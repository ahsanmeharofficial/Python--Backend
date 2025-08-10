# Pehli list
boysList = ["Ahsan", "Bilal", "Usman"]

# Doosri list
girlsList = ["Sana", "Hina", "Kiran"]

# Concatenation ka use (+ operator)
classList = boysList + girlsList

print("Boys List:", boysList)
print("Girls List:", girlsList)
print("Class List:", classList)
# Note: Concatenation se naya list banta hai, original lists change nahi hoti


# extend() vs concatenation (+) difference:

# 1) extend():
#    - Original list ko modify karta hai
#    - Doosri list ke elements ko directly pehli list ke end me dalta hai
#    - Nayi list create nahi karta

# 2) concatenation (+):
#    - Original lists ko change nahi karta
#    - Dono lists ko jod kar ek nayi list return karta hai
#    - Purani lists waisi ki waisi rehti hain
