# Default Arguments in Python
# Default arguments woh hote hain jin ki value function define karte waqt set kar di jati hai.
# Agar function ko call karte waqt koi value nahi di jati, to default value use hoti hai.

print("befor add function.")

# Function ko parameters ke sath define kiya gaya hai (default values ke sath)
def add(num1, num2 , num3=10):
    result = num1 + num2 + num3
    print(result)

# Yahan function bina arguments ke call ho raha hai, to default values (5, 10) use hongi
add(5,5)  # num1 = 5, num2 = 10

print("after add functions.")

# Yahan function ko arguments ke sath call kiya gaya hai, to wohi values use hongi



add(5, 5, 20)  # num1 = 5, num2 = 5, num3 = 20


# note  defult argument ka matlb ha k ager hum na 3 values add ki han to ager hum 2 values dan ga t0 vo add ker da ga 