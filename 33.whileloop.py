i=1
while i<=5:
    print("pakistan zinda bad",i)
    i=i+1
print("end of loop")


# User se number aur count lena (currently unused in loop)
num = int(input("Enter a number: "))
count = int(input("Enter the count: "))

# Input aur output lists
inputList = [10, 20, 30, 40, 50]
outputList = []  # Start empty so hum while loop me fill karein

# Counter
i = 0  # Index 0 se start karte hain

# Jab tak i list ki length se chhota hai, loop chalega
while i < len(inputList):
    # Har element ka 2 se multiplication
    required = inputList[i] * 2

    # Result ko output list me add karna
    outputList.append(required)

    # i ko increment karna
    i += 1

# Output print karna
print("After while:", outputList)






#example
# Original list
inputList = [10, 21, 30, 41, 50, 63, 72, 85]

# Even aur Odd store karne ke liye empty lists
evenList = []
oddList = []

# While loop ka use
i = 0
while i < len(inputList):
    # Check agar number even hai
    if inputList[i] % 2 == 0:
        evenList.append(inputList[i])
    else:
        oddList.append(inputList[i])
    i += 1

# Results print karo
print("Even Numbers:", evenList)
print("Odd Numbers:", oddList)




#exmaple find the reminder witout using modulus operator
# Original list
inputList = [10, 21, 30, 41, 50, 63, 72, 85]    
# Reminder store karne ke liye empty list
reminderList = []   
# While loop ka use
i = 0
while i < len(inputList):
    # Calculate reminder
    reminder = inputList[i]
    while reminder >= 10:  # Assuming we want to find reminder with respect to
        reminder -= 10
    reminderList.append(reminder)
    i += 1
# Results print karo
print("Reminders:", reminderList)
