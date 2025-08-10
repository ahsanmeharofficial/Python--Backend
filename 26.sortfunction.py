studentNames = ["Ahsan", "Bilal", "Usman", "Shahzad", "Ihsan"]

# sort() ka use:
# Ye list ko A-Z ke order mein arrange karega
studentNames.sort()

print("Ascending order:", studentNames)

# Agar Z-A order chahiye to reverse=True use karo
studentNames.sort(reverse=True)
print("Descending order:", studentNames)
# Note: sort() method list ko modify karta hai, naya list nahi banata