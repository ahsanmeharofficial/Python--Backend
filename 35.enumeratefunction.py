# List of names
userNames = ["ahmed", "omar", "ali", "zain", "hassan"]

# For loop ke sath enumerate use kar rahe hain taake index bhi mile
for indexNumber, nameValue in enumerate(userNames):
    # Check kar rahe hain ke current name 'ali' hai ya nahi
    if nameValue == "ali":
        print("Name 'ali' found at index:", indexNumber)  # Ali ka index print karega
        break  # Loop yahan ruk jayega kyun ke name mil gaya
# For loop with enumerate to get index and value