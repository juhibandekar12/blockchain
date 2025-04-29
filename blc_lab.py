import time
import hashlib
import json

# -------------------------
# 🧱 Genesis Block Creation
# -------------------------
blockchain = [
    {
        "index": 0,
        "timestamp": time.time(),
        "data": {"info": "Genesis Block"},
        "previous_hash": "0",
        "hash": hashlib.sha256("Genesis Block".encode()).hexdigest()
    }
]

# -------------------------
# ➕ Add a New Block
# -------------------------
def add_block(student_id, name, grades):
    previous_block = blockchain[-1]
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

    blockchain.append(new_block)
    print(f"\n✅ Block {index} added for {name}!\n")

# -------------------------
# 🖨️ Display the Blockchain
# -------------------------
def display_blockchain():
    print("\n📜 Final Blockchain:")
    print(json.dumps(blockchain, indent=4))

# -------------------------
# 👨‍🏫 Interactive Input Loop
# -------------------------
while True:
    print("\nEnter student report card data (or type 'exit' to quit):")
    student_id = input("Student ID: ")
    if student_id.lower() == "exit":
        break
    name = input("Student Name: ")

    grades = {}
    print("Enter subject and grade (type 'done' when finished):")
    while True:
        subject = input("Subject: ")
        if subject.lower() == "done":
            break
        grade = input("Grade: ")
        grades[subject] = grade

    add_block(student_id, name, grades)

# -------------------------
# 🖨️ Print Blockchain at End
# -------------------------
display_blockchain()
# -------------------------
# 🖨️ Display the Blockchain with Hashes
# -------------------------
def display_blockchain():
    print("\n📜 Final Blockchain with Hashes:\n")
    for block in blockchain:
        print(f"Block Index   : {block['index']}")
        print(f"Timestamp     : {block['timestamp']}")
        print(f"Student Data  : {json.dumps(block['data'], indent=2)}")
        print(f"Previous Hash : {block['previous_hash']}")
        print(f"Current Hash  : {block['hash']}")
        print("-" * 60)

