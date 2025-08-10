# copy() ka use:
# Ye ek list ki duplicate copy banata hai
# Nayi list banne ke baad, original list me change ka effect copy par nahi hota

studentNames = ["Ahsan", "Bilal", "Usman"]
copiedNames = studentNames.copy()

print("Original List:", studentNames)
print("Copied List:", copiedNames)
# Agar original list me koi change karein, to copied list par effect nahi hoga



# clear() ka use:
# Ye list ke andar ke saare elements remove kar deta hai
# List empty ho jati hai lekin variable phir bhi exist karta hai

studentNames.clear()
print("Cleared List:", studentNames)  # Output: []
# Note: clear() method list ko modify karta hai, naya list nahi banata
# Agar clear() ke baad list ko print karein, to wo empty list dikh