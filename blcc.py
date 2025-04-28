import streamlit as st
import hashlib

# Initialize hospital school attendance ledger in session state
if 'hospital_school_attendance_ledger' not in st.session_state:
    st.session_state.hospital_school_attendance_ledger = []

# Function to create a hash of a record
def generate_hash(record):
    record_str = f"{record['student_name']}{record['date']}{record['status']}{record['previous_hash']}"
    return hashlib.sha256(record_str.encode()).hexdigest()

# Function to add an attendance record
def add_student_attendance(student_name, date, status):
    previous_hash = (
        st.session_state.hospital_school_attendance_ledger[-1]["hash"]
        if st.session_state.hospital_school_attendance_ledger
        else "0"
    )

    record = {
        "student_name": student_name,
        "date": str(date),
        "status": status,
        "previous_hash": previous_hash
    }

    # Generate the hash
    record["hash"] = generate_hash(record)

    # Add the record
    st.session_state.hospital_school_attendance_ledger.append(record)
    st.success(f"✅ Attendance recorded for {student_name} on {date} as {status}.")

# Streamlit app layout
st.title("🏥 Hospital School Attendance Ledger (with Hashing)")

st.subheader("➕ Add New Attendance Record")

# Inputs
student_name = st.text_input("Student Name")
date = st.date_input("Date of Attendance")
status = st.selectbox("Status", ["Present", "Absent"])

# Button
if st.button("Add Attendance Record"):
    if student_name.strip() == "":
        st.error("Please enter the student's name.")
    else:
        add_student_attendance(student_name, date, status)

st.divider()

# Display ledger
st.subheader("📋 Ledger Records")

if st.session_state.hospital_school_attendance_ledger:
    for idx, record in enumerate(st.session_state.hospital_school_attendance_ledger):
        st.markdown(f"### Record {idx+1}")
        st.json(record)
else:
    st.info("No records yet. Please add attendance.")


