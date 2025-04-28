import streamlit as st

# Initialize hospital ledger in session state if it doesn't exist
if 'hospital_ledger' not in st.session_state:
    st.session_state.hospital_ledger = []

st.title("Hospital Ledger Management")

st.header("Add a Patient Visit")

# Create input fields for patient details
patient_name = st.text_input("Enter the patient's name")
treatment = st.text_input("Enter the treatment received")
cost = st.number_input("Enter the cost of the treatment ($)", min_value=0.0, step=0.01)

# Button to add visit
if st.button("Add Visit"):
    if patient_name and treatment:
        # Create a dictionary for the visit
        visit = {
            "patient_name": patient_name,
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
        st.write(f"*Patient:* {visit['patient_name']}  |  *Treatment:* {visit['treatment']}  |  *Cost:* ${visit['cost']}")
