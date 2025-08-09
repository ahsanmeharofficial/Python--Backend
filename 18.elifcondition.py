# if condition
# # Example: Weather check
# Example 1: Weather Check
temperature = 25    
if temperature > 30:  # agar temperature 30 se zyada hai
    print("It's hot today")  # garam hai
elif temperature > 20:  # agar temperature 20 se zyada hai
    print("It's warm today")  # garam hai
else:  # warna
    print("It's cold today")  # garam hai
    
    
# Example 2: Grade Check
marks = 85
if marks >= 90:  # agar marks 90 se zyada hai
    print("Grade: A")  # A grade    
elif marks >= 80:  # agar marks 80 se zyada hai
    print("Grade: B")  # B grade
elif marks >= 70:  # agar marks 70 se zyada hai
    print("Grade: C")  # C grade
elif marks >= 60:  # agar marks 60 se zyada hai
    print("Grade: D")  # D grade    
    
    
    
# First condition check
# agar temperature 30 se zyada hai
# yeh tab chalega jab pehla condition True ho

# Second condition check (only runs if first condition was False)
# agar pehla False tha aur yeh True hai
# yeh tab chalega jab dusra condition True ho

# If none of the above conditions are True
# jab upar dono False hon
# yeh tab chalega jab dono False ho
