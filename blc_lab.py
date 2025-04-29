import streamlit as st
import time
import hashlib
import json

# -------------------------
# 🧱 Genesis Block Creation
# -------------------------
@st.cache_data
def create_genesis_block():
    return [
        {
            "index": 0,
            "timestamp": time.time(),
            "data": {"info": "Genesis Block"},
            "previous_hash": "0",
            "hash": hashlib.sha256("Genesis Block".encode()).hexdigest()
        }
    ]

# Initialize blockchain
if "blockchain" not in st.session_state:
    st.session_state.blockchain = create_genesis_block()

# -------------------------
# ➕ Add a New Block
# -------------------------
def add_block(student_id, name, grades):
    previous_block = st.session_state.blockchain[-1]
    index = previous_block["index"] + 1
    timestamp = time.time()
    previous_hash = previous_block["hash"]

    # Prepare data
    data = {
        "student_id": student_id,
        "name": name,
        "grades": grades
    }

    # Convert data to JSON string for hashing
    block_string = f"{index}{timestamp}{json.dumps(data, sort_keys=True)}{previous_hash}"
    block_hash = hashlib.sha256(block_string.encode()).hexdigest()

    # Create new block
    new_block = {
        "index": index,
        "timestamp": timestamp,
        "data": data,
        "previous_hash": previous_hash,
        "hash": block_hash
    }

    st.session_state.blockchain.append(new_block)
    st.success(f"✅ Block {index} added for {name}!")

# -------------------------
# 🖨️ Display the Blockchain
# -------------------------
def display_blockchain():
    st.subheader("📜 Final Blockchain with Hashes")
    for block in st.session_state.blockchain:
        with st.expander(f"Block {block['index']} - {block['data'].get('name', 'Genesis Block')}"):
            st.write(f"**Block Index:** {block['index']}")
            st.write(f"**Timestamp:** {time.ctime(block['timestamp'])}")
            st.write(f"**Student Data:**")
            st.json(block['data'])
            st.write(f"**Previous Hash:** `{block['previous_hash']}`")
            st.write(f"**Current Hash:** `{block['hash']}`")

# -------------------------
# 🎯 Streamlit App
# -------------------------
st.title("📚 Student Report Card Blockchain")

with st.form("Add Student Block"):
    st.subheader("➕ Enter Student Report Card Data")
    student_id = st.text_input("Student ID")
    name = st.text_input("Student Name")

    st.markdown("**Enter subjects and grades:**")
    subjects = {}
    subject = st.text_input("Subject 1", key="subject1")
    grade = st.text_input("Grade 1", key="grade1")
    if subject and grade:
        subjects[subject] = grade

    subject2 = st.text_input("Subject 2", key="subject2")
    grade2 = st.text_input("Grade 2", key="grade2")
    if subject2 and grade2:
        subjects[subject2] = grade2

    subject3 = st.text_input("Subject 3", key="subject3")
    grade3 = st.text_input("Grade 3", key="grade3")
    if subject3 and grade3:
        subjects[subject3] = grade3

    submitted = st.form_submit_button("Add Block")
    if submitted:
        if student_id and name and subjects:
            add_block(student_id, name, subjects)
        else:
            st.error("⚠️ Please fill all fields and at least one subject and grade.")

st.divider()

# Blockchain Viewer
display_blockchain()
