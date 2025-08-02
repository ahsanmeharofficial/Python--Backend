userName = ("mian ahsan")  # userName variable me aik string store ki hai
num = 1  # num variable me aik integer value store ki hai

# id() function RAM me variable ki unique address batata hai
print(id(userName))  # userName ka RAM address print hoga
print(num)  # num ki value print hogi

# Python case sensitive language hai, yani variable ka naam chota ya bara ho to alag samjha jata hai

# 1. camelCase: pehla word chota, agla word capital se shuru hota hai (userName)
# 2. PascalCase: har word capital se shuru hota hai (UserName)
# 3. snake_case: words ko underscore se alag karte hain (user_name)

num = 20 * 5  # yahan pehle multiplication hogi, phir value num me store hogi
print(num)  # result print hoga

num = 2 * 2 - 1 + 3 / 2  # yahan PEMDAS rule follow hoga
# PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print(num)  # final result print hoga

# Neeche kuch aur examples hain concept clear karne ke liye

# Example 1
result = 5 + 3 * 2  # pehle 3*2=6, phir 5+6=11
print(result)  # 11

# Example 2
result = (5 + 3) * 2  # pehle (5+3)=8, phir 8*2=16
print(result)  # 16

# Example 3
result = 10 - 4 / 2 + 6  # pehle 4/2=2.0, phir 10-2.0=8.0, phir 8.0+6=14.0
print(result)  # 14.0

# Example 4
result = 2 + 3 * 4 - 1  # pehle 3*4=12, phir 2+12=14, phir 14-1=13
print(result)  # 13

# Example 5
result = 2 * 2 - 1 + 3 / 2  # pehle 2*2=4, phir 3/2=1.5, phir 4-1=3, phir 3+1.5=4.5
print(result)  # 4.5

userName = ("ali")  # userName ki value change kar di
print(userName)  # ab "ali" print hoga