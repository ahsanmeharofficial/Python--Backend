# Python mein list se element remove karne ke liye remove() function ka use karte hain
fruitList = ["apple", "banana", "mango", "orange"]

# remove() ka use:
# Ye list se wo element hata deta hai jo tum value ke taur pe dete ho
# Yahan hum "mango" ko remove kar rahe hain
fruitList.remove("mango")

# Updated list print karein
print(fruitList)  # Output: ['apple', 'banana', 'orange']
# Note: Agar tum value ko list mein nahi paate, to ye error dega
# Isliye ensure karo ke value list mein hai pehle