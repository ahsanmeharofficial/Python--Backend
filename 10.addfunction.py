# Ek simple add function jo do numbers ko add karta hai

print("Function se pehle yeh line chalegi.")

# Ab function ko parameters ke sath define karte hain (default values ke sath)
def addNumbers(num1, num2):
    result = num1 + num2
    print(result)

# Function ko bina arguments ke call karenge to default values use hongi
addNumbers(10,20)

print("Function ke baad yeh line chalegi.")

# Function ko arguments ke sath call karenge to woh values use hongi
addNumbers(100, 200)
addNumbers(50, 75)
addNumbers(0, 0)
addNumbers(-5, -10)
addNumbers(3.5, 2.5)