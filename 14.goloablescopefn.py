# Local aur Global Scope in Python -
# Global variable wo hota hai jo function ke bahar banaya jata hai, aur har jaga use ho sakta hai.
# Local variable wo hota hai jo function ke andar banaya jata hai, aur sirf usi function ke andar use ho sakta hai.

# Global variable
num = 10

def showScope():
    # Local variable
    message = "Yeh local variable hai"
    print("Global variable ka value:", num)      # Global variable use ho sakta hai
    print("Local variable ka value:", message)   # Local variable sirf yahan use ho sakta hai

showScope()

# Global variable ko function ke bahar bhi use kar sakte hain
print("Global variable function ke bahar bhi use ho sakta hai:", num)

# Lekin local variable function ke bahar use nahi ho sakta
# print(message)  # Error aayegi, kyun ke 'message' sirf function ke andar hai







# Example: Adding and return function with global variable
def addWithGlobal(value):
    # num global variable hai, value local hai
    result = num + value
    return result

sumResult = addWithGlobal(5)
print("Global variable aur local value ka sum:", sumResult)



# Global aur Local Scope ka concept samajhne ke liye example

c = 10  # yeh global variable hai

def sum(a, b):
    c = a + b  # yeh local variable hai, jo function ke andar hai
    print("Function ke andar ke local variables:", locals())  # local variables ko print karega
    return c  # local variable c ko return karega

d = sum(10, 20)  # function ko call karte hain aur result ko d mein store karte hain
print("Function ka result (local c):", d)
print("Global variable c ki value:", c)  # global variable c ki value print karte hain

# by sir naveed sarwar 
num = 10
message = None  # Pehle global bana diya

def showScope():
    global message
    message = "Yeh local variable ab global ban gaya"
    print("Global variable ka value:", num)
    print("Local/Global message ka value:", message)

showScope()
print("Function ke bahar bhi message ka value:", message)
# Global variable ko function ke andar modify karne ke liye 'global' keyword ka use karna padta hai
# Agar aapko function ke andar kisi global variable ko modify karna hai, to '