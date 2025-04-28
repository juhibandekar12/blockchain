import hashlib

# Initialize an empty hospital school attendance ledger
hospital_school_attendance_ledger = []

# Function to create a hash of a record
def generate_hash(record):
    record_str = f"{record['student_name']}{record['date']}{record['status']}{record['previous_hash']}"
    return hashlib.sha256(record_str.encode()).hexdigest()

# Function to add an attendance record
def add_student_attendance(student_name, date, status):
    # Get the previous hash (last record's hash) or "0" if this is the first record
    previous_hash = hospital_school_attendance_ledger[-1]["hash"] if hospital_school_attendance_ledger else "0"

    # Create a new attendance record
    record = {
        "student_name": student_name,
        "date": date,
        "status": status,
        "previous_hash": previous_hash
    }

    # Generate a hash for this record
    record["hash"] = generate_hash(record)

    # Add the record to the ledger
    hospital_school_attendance_ledger.append(record)
    print(f"Attendance recorded for {student_name} on {date}: {status}.")

# Adding attendance records
add_student_attendance("Alice Brown", "2025-04-25", "Present")
add_student_attendance("Bob Smith", "2025-04-25", "Absent")
add_student_attendance("Alice Brown", "2025-04-26", "Present")
add_student_attendance("Charlie Davis", "2025-04-25", "Present")

# Display the hospital school attendance ledger
print("\nHospital School Attendance Ledger with Hashing:")
for record in hospital_school_attendance_ledger:
    print(record)
