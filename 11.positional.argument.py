# Positional (ya Required) Arguments in Python 
# Positional arguments woh hote hain jo function ko call karte waqt sahi order mein dene zaroori hote hain.
# Agar aap function ko bina arguments ke call karte hain aur default values di hui hain, to woh default values use hongi.
# Lekin agar aap values dete hain, to woh values order ke hisaab se parameters mein assign ho jati hain.

print("befor add function.")

# Function ko parameters ke sath define kiya gaya hai (default values ke sath)
def add(num1, num2):
    result = num1 + num2
    print(result)

# Yahan function bina arguments ke call ho raha hai, to default values (5, 10) use hongi
add(10, 20)  # num1 = 10, num2 = 20

print("after add functions.")

# Yahan function ko arguments ke sath call kiya gaya hai
# 100 num1 mein jayega, 200 num2 mein jayega (order matter karta hai)
add(100, 200)
add(200, 100)
add(100, 100)


   # note    phala argument phala num1 ma store higa, dosra argument dosra num2 ma store hoga
# Agar aap function ko bina kisi argument ke call karte hain, to error aay