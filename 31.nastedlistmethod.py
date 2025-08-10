# Nested list: Har class ke students ki alag list
classes = [
    ["Ahsan", "Bilal", "Usman"],     # Class 1 students
    ["Sana", "Hina", "Kiran"],       # Class 2 students
    ["Shahzad", "Ihsan", "Zubair"]   # Class 3 students
]

# Puri nested list print karo
print("All Classes:", classes)

# Specific class ka data (Class 2)
print("Class 2 Students:", classes[1])

# Nested list ke andar specific student (Class 1 ka 2nd student)
print("Class 1 ka 2nd student:", classes[0][1])
# Nested list ke andar sab students ka naam print karo