# Return Function in Python - Beginner Level
# "return" ka use function ke andar se value bahar bhejne ke liye hota hai.

print("Function se pehle yeh line chalegi.")

# Ek simple function jo do numbers ko add karta hai aur result return karta hai
def addNumbers():
    num1 = 3
    num2 = 7
    result = num1 + num2
    return result  # Yeh result function ke bahar mil jayega

# Function ko call karte hain aur uski value print karte hain
sumResult = addNumbers()
print("Add function ka result hai:", sumResult)

print("Function ke baad yeh line chalegi.")