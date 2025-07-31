# Addition (jama karna)
numA = 7
numB = 3
additionResult = numA + numB  # yahan hum 7 aur 3 ko jama kar rahe hain
print("Addition Result (7 + 3):", additionResult)

# Subtraction (minus karna)
numC = 15
numD = 8
subtractionResult = numC - numD  # yahan hum 15 me se 8 minus kar rahe hain
print("Subtraction Result (15 - 8):", subtractionResult)

# Multiplication (zaarib karna)
numE = 4
numF = 6
multiplicationResult = numE * numF  # yahan hum 4 aur 6 ko multiply kar rahe hain
print("Multiplication Result (4 * 6):", multiplicationResult)

# Division (taqseem karna)
numG = 20
numH = 4
divisionResult = numG / numH  # yahan hum 20 ko 4 se divide kar rahe hain
print("Division Result (20 / 4):", divisionResult)

# Modulus (baqi nikalna)
numI = 17
numJ = 5
modulusResult = numI % numJ  # yahan hum 17 ko 5 se divide kar ke remainder nikal rahe hain
print("Modulus Result (17 % 5):", modulusResult)

# Exponentiation (taqat ya power nikalna)
baseNumber = 2
powerNumber = 3
exponentiationResult = baseNumber ** powerNumber  # yahan hum 2 ki power 3 nikal rahe hain
print("Exponentiation Result (2 ** 3):", exponentiationResult)

# Floor Division (integer division, point ke baad sab kuch hata dena)
numK = 19
numL = 5
floorDivisionResult = numK // numL  # yahan hum 19 ko 5 se divide kar ke sirf integer part le rahe hain
print("Floor Division Result (19 // 5):", floorDivisionResult)

# Extra: Negative Numbers Example (manfi numbers ka istemal)
negativeResult = -10 + 5  # yahan hum -10 aur 5 ko jama kar rahe hain
print("Addition with Negative Number (-10 + 5):", negativeResult)

# Extra: Zero Division Example (zero se divide karne ki koshish)
try:
    zeroDivisionResult = 10 / 0  # yahan hum 10 ko 0 se divide kar rahe hain (ye error dega)
except ZeroDivisionError:
    print("Division by Zero Error: 10 ko 0 se divide nahi kar sakte!")

# Extra: Floating Point Example (desi numbers ka istemal)
floatResult = 7.5 + 2.3  # yahan hum 7.5 aur 2.3 ko jama kar rahe hain
print("Addition with Floating Point (7.5 + 2.3):", floatResult)

# DMAS Rule Example (Order of Operations ka istemal)
# DMAS ka matlab hai: Division, Multiplication, Addition, Subtraction
dmasExpression = 10 + 5 * 2 - 8 / 4  # yahan pehle multiplication aur division hoga, phir addition aur subtraction
print("DMAS Rule Example (10 + 5 * 2 - 8 / 4):", dmasExpression)
# Pehle 5*2 (10), phir 8/4 (2), phir 10+10 (20), phir 20-2 (18)