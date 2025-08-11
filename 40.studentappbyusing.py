# Python program to manage a student application with basic CRUD operations2
# Default 5 students ka data (dictionary list form me)
studentsList = [
    {"id": 1, "name": "Ali", "email": "ali@example.com"},
    {"id": 2, "name": "Ahmed", "email": "ahmed@example.com"},
    {"id": 3, "name": "Omar", "email": "omar@example.com"},
    {"id": 4, "name": "Zain", "email": "zain@example.com"},
    {"id": 5, "name": "Hassan", "email": "hassan@example.com"}
]

# --- Show all student emails ---
print("All Student Emails:")
for student in studentsList:
    print(student["email"])  # Roman Urdu: Har student ka email print kar rahe hain

# --- Add new student ---
newStudent = {"id": 6, "name": "Saad", "email": "saad@example.com"}
studentsList.append(newStudent)  # Roman Urdu: New student add kiya
print("\nNew student added!")

# --- Update student by ID using map ---
updateId = int(input("\nEnter student ID to update: "))  # Roman Urdu: User se ID le rahe hain
newName = input("Enter new name: ")  # Roman Urdu: Naya name le rahe hain
newEmail = input("Enter new email: ")  # Roman Urdu: Naya email le rahe hain

studentsList = list(map(lambda student: 
    {**student, "name": newName, "email": newEmail} if student["id"] == updateId else student, 
    studentsList))

print("\nStudent updated successfully!")
print("Updated Values:")
for student in studentsList:
    if student["id"] == updateId:
        print(student)  # Roman Urdu: Sirf updated student ka data print kar rahe hain

# --- Delete student by ID using filter ---
removeId = int(input("\nEnter student ID to remove: "))  # Roman Urdu: Remove karne ke liye ID le rahe hain
studentsList = list(filter(lambda student: student["id"] != removeId, studentsList))

print("\nStudent removed successfully!")

# --- Show all student emails after update & delete ---
print("\nUpdated Student Emails:")
for student in studentsList:
    print(student["email"])
