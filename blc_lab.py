import streamlit as st
import hashlib
import time
import json

# -------------------------
# Initialize Blockchain
# -------------------------
def create_genesis_block():
    genesis_data = {"info": "Genesis Block"}
    genesis_hash = hashlib.sha256("Genesis Block".encode()).hexdigest()
    return {
        "index": 0,
        "timestamp": time.time(),
        "data": genesis_data,
        "previous_hash": "0",
        "hash": genesis_hash
    }

if "blockchain" not in st.session_state:
    st.session_state.blockchain = [create_genesis_block()]

# -------------------------
# Hashing Function
# -------------------------
def compute_hash(index, timestamp, data, previous_hash):
    block_string = f"{index}{timestamp}{json.dumps(data, sort_keys=True)}{previous_hash}"
    return hashlib.sha256(block_string.encode()).hexdigest()

# -------------------------
# Add a New Block
# -------------------------
def add_block(student_id, name, grades):
    previous_block = st.session_state.blockchain[-1]
    index = previous_block["index"] + 1
    timestamp = time.time()
    previous_hash = previous_block["hash"]

    data = {
        "student_id": student_id,
        "name": name,
        "grades": grades
    }

    block_hash = compute_hash(index, timestamp, data, previous_hash)

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
# Streamlit App UI
# -------------------------
st.title("📘 School Report Card Blockchain")

st.subheader("➕ Add Student Report Card")
with st.form("add_form", clear_on_submit=True):
    student_id = st.text_input("Student ID")
    name = st.text_input("Student Name")
    subjects_input = st.text_area("Enter subjects and grades (e.g., Math:A, English:B+)", height=100)

    submitted = st.form_submit_button("Add to Blockchain")

    if submitted:
        if not student_id or not name or not subjects_input:
            st.warning("Please fill in all fields.")
        else:
            grades = {}
            try:
                pairs = subjects_input.split(",")
                for pair in pairs:
                    subject, grade = pair.strip().split(":")
                    grades[subject.strip()] = grade.strip()
                add_block(student_id, name, grades)
            except Exception as e:
                st.error(f"❌ Invalid input format. Use 'Subject:Grade'. Error: {e}")

# -------------------------
# Display Blockchain
# -------------------------
st.subheader("📜 Blockchain Explorer")

for block in st.session_state.blockchain:
    with st.expander(f"🔗 Block {block['index']} - {block['data'].get('name', 'Genesis')}"):
        st.write(f"**Index:** {block['index']}")
        st.write(f"**Timestamp:** {block['timestamp']}")
        st.write("**Data:**")
        st.json(block["data"])
        st.write(f"**Previous Hash:** `{block['previous_hash']}`")
        st.write(f"**Current Hash:** `{block['hash']}`")
