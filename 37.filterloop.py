# List of numbers
numbersList = [1, 2, 3, 4, 5, 6]

# Filter function ka use:
# Filter ka kaam hota hai ke list ke sirf un elements ko rakhe jo given condition ko pass karein
# Yahan hum sirf even (joday) numbers ko filter kar rahe hain
evenNumbers = list(filter(lambda x: x % 2 == 0, numbersList))

# Nayi filtered list print karna
print(evenNumbers)  # Output: [2, 4, 6]
