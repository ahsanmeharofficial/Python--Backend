# Membership Operators in Python
# Membership operators ka use check karne ke liye hota hai ke koi value kisi list, string, ya tuple mein hai ya nahi.
# Do main operators hain: "in" aur "not in"
# Hum logical operators (and, or) bhi membership ke sath use kar sakte hain.

# Example 1: List ke andar value check karna
fruits = ["apple", "banana", "mango"]

print("apple in fruits:", "apple" in fruits)        # True
print("orange in fruits:", "orange" in fruits)      # False

# Example 2: String ke andar character check karna
message = "hello world"

print("'h' in message:", 'h' in message)            # True
print("'z' in message:", 'z' in message)            # False

# Example 3: Tuple ke andar value check karna
numbers = (1, 2, 3, 4, 5)

print("3 in numbers:", 3 in numbers)                # True
print("10 in numbers:", 10 in numbers)              # False

# Example 4: "not in" ka use
print("banana not in fruits:", "banana" not in fruits)  # False
print("grape not in fruits:", "grape" not in fruits)    # True

# Example 5: Membership + Logical Operators
# Check karen kya "apple" fruits mein hai AUR "banana" bhi hai?
print("apple AND banana in fruits:", ("apple" in fruits) and ("banana" in fruits))  # True

# Check karen kya "apple" fruits mein hai YA "grape" hai?
print("apple OR grape in fruits:", ("apple" in fruits) or ("grape" in fruits))      # True

# Check karen kya "orange" fruits mein nahi hai AUR "mango" hai?
print("orange not in fruits AND mango in fruits:", ("orange" not in fruits) and ("mango" in fruits))  # True