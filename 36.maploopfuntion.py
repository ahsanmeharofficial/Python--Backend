# List of numbers
numbersList = [1, 2, 3, 4, 5]

# Map loop ka basic use (har number ko 2 se multiply karna)
newList = list(map(lambda x: x * 2, numbersList))

# Nayi list print karna
print(newList)
# Output: [2, 4, 6, 8, 10]



# Map function ka use:
# Map ka kaam hota hai ke ek function ko list ke har element par apply kare
# Yani aap ek hi jagah logic likho aur wo list ke sab elements par chale
# Yahan hum har number ko 2 se multiply kar rahe hain
# Map ka use hota hai jab hum ek list ke sab elements ko ek aisa logic par apply karna hai
