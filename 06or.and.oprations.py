# Logical Operators (AND, OR, NOT) in Python 
# Logical operators ka use hum do ya zyada conditions ko check karne ke liye karte hain.
# "and" ka matlab hai dono conditions sahi honi chahiye.
# "or" ka matlab hai koi bhi aik condition sahi ho to result sahi hoga.
# "not" ka matlab hai condition ko ulta kar dena (True ko False aur False ko True).

# Variables 
numOne = 10
numTwo = 20
numThree = 30

# AND operator ka example
# Check karen kya numOne 10 hai AND numTwo 20 hai?
resultAnd = (numOne == 10) and (numTwo == 20)
print("Kya numOne 10 hai AUR numTwo 20 hai? (and):", resultAnd)

# OR operator ka example
# Check karen kya numOne 5 hai YA numThree 30 hai?
resultOr = (numOne == 5) or (numThree == 30)
print("Kya numOne 5 hai YA numThree 30 hai? (or):", resultOr)

# Aur ek example: dono galat
resultBothFalse = (numOne == 5) and (numTwo == 25)
print("Kya numOne 5 hai AUR numTwo 25 hai? (and):", resultBothFalse)

# Aur ek example: dono sahi
resultBothTrue = (numOne == 10) or (numTwo == 20)
print("Kya numOne 10 hai YA numTwo 20 hai? (or):", resultBothTrue)

# NOT operator ka example
# Check karen kya numOne 10 nahi hai?
resultNot = not (numOne == 10)
print("Kya numOne 10 nahi hai? (not):", resultNot)

# NOT operator ka ek aur example
# Check karen kya numTwo 15 nahi hai?
resultNotTwo = not (numTwo == 15)
print("Kya numTwo 15 nahi hai? (not):", resultNotTwo)