# Division Operators in Python - Beginner Level
# Division operator (/) ka use hum do ya zyada numbers ko divide karne ke liye karte hain.
# Neeche kuch asaan examples diye gaye hain jo aapko division samajhne mein madad karenge.
# Hum camelCase variable names aur simple numbers use karenge.

# Variables banate hain
numOne = 100
numTwo = 5
numThree = 2

# Basic division ka example
# numOne ko numTwo se divide karen
resultOne = numOne / numTwo
print("numOne ko numTwo se divide karne ka result:", resultOne)  # 100 / 5 = 20.0

# Multiple division ka example
# numOne ko numTwo se, phir result ko numThree se divide karen
resultTwo = numOne / numTwo / numThree
print("numOne ko numTwo aur numThree se divide karne ka result:", resultTwo)  # (100 / 5) / 2 = 10.0

# Ek aur example: chote numbers ke sath
smallNum = 20
smallerNum = 4
smallestNum = 2

resultThree = smallNum / smallerNum / smallestNum
print("smallNum ko smallerNum aur smallestNum se divide karne ka result:", resultThree)  # (20 / 4) / 2 = 2.5

# Division by 1 ka example (koi bhi number 1 se divide ho to wahi number aata hai)
resultFour = numOne / 1
print("numOne ko 1 se divide karne ka result:", resultFour)  # 100 / 1 = 100.0

# Division by itself ka example (koi bhi number apne aap se divide ho to result 1 aata hai)
resultFive = numTwo / numTwo
print("numTwo ko numTwo se divide karne ka result:", resultFive)  # 5 / 5 = 1.0