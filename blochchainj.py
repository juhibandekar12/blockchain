import streamlit as st
import hashlib
import json

# Initialize the hospital ledger (stored in session state for persistence)
if 'hospital_ledger' not in st.session_state:
    st.session_state.hospital_ledger = {}

def generate_hash(patient_name, treatment, cost, date_of_visit):
    """Generate a hash to ensure data integrity."""
    data = f"{patient_name}{treatment}{cost}{date_of_visit}"
    return hashlib.md5(data.encode()).hexdigest()

# Streamlit app layout
st.title("🏥 Hospital Ledger System")

# Sidebar navigation
menu = st.sidebar.radio("Navigation", ["Add Patient Visit", "Search Patient Records"])

if menu == "Add Patient Visit":
    st.header("Add or Update Patient Visit")
    
    with st.form("patient_form"):
        patient_name = st.text_input("Patient Name").strip().lower()
        treatment = st.text_input("Treatment Received")
        cost = st.number_input("Cost of Treatment ($)", min_value=0.0, format="%.2f")
        date_of_visit = st.date_input("Date of Visit")
        submit_button = st.form_submit_button("Add Visit")
    
    if submit_button:
        if patient_name and treatment and cost > 0:
            visit_hash = generate_hash(patient_name, treatment, cost, str(date_of_visit))
            visit = {
                "treatment": treatment,
                "cost": cost,
                "date_of_visit": str(date_of_visit),
                "visit_hash": visit_hash
            }
            
            if patient_name not in st.session_state.hospital_ledger:
                st.session_state.hospital_ledger[patient_name] = []
            
            st.session_state.hospital_ledger[patient_name].append(visit)
            
            st.success(f"Visit added for {patient_name.capitalize()} on {date_of_visit}.")
            st.json(visit)
        else:
            st.error("Please fill in all fields correctly.")

elif menu == "Search Patient Records":
    st.header("Search Patient Visits")
    search_name = st.text_input("Enter patient name to search").strip().lower()
    
    if search_name:
        if search_name in st.session_state.hospital_ledger:
            st.subheader(f"Visit records for {search_name.capitalize()}")
            for visit in st.session_state.hospital_ledger[search_name]:
                st.json(visit)
        else:
            st.warning("Patient not found in the ledger.")
