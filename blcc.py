import streamlit as st
import hashlib

# Initialize hospital ledger in session state if it doesn't exist
if 'hospital_ledger' not in st.session_state:
    st.session_state.hospital_ledger = []

st.title("Hospital Ledger Management")

st.header("Add a Patient Visit")

# Create input fields for patient details
patient_name = st.text_input("Enter the patient's name")
treatment = st.text_input("Enter the treatment received")
cost = st.number_input("Enter the cost of the treatment ($)", min_value=0.0, step=0.01)

# Function to create a hash for a patient's name
def generate_patient_hash(patient_name):
    return hashlib.sha256(patient_name.encode()).hexdigest()

# Button to add visit
if st.button("Add Visit"):
    if patient_name and treatment:
        # Generate a unique hash for the patient's name
        patient_hash = generate_patient_hash(patient_name)
        
        # Create a dictionary for the visit with hashed patient name
        visit = {
            "patient_name_hash": patient_hash,
            "patient_name": patient_name,  # Keep original name for display (can be omitted for privacy)
            "treatment": treatment,
            "cost": cost
        }
        
        # Add the visit to the hospital ledger
        st.session_state.hospital_ledger.append(visit)
        st.success(f"Visit added for {patient_name} with treatment {treatment} costing ${cost}.")
    else:
        st.error("Please fill in all the fields.")

# Display the hospital ledger
if st.session_state.hospital_ledger:
    st.header("Hospital Ledger")
    for visit in st.session_state.hospital_ledger:
        # Display the original patient name along with the hashed value
        st.write(f"*Patient:* {visit['patient_name']} (Hash: {visit['patient_name_hash']})  |  *Treatment:* {visit['treatment']}  |  *Cost:* ${visit['cost']}")
