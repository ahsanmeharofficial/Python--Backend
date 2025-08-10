studentNames = ["Ahsan", "Bilal", "Usman", "Sana", "Hina", "Shahzad", "Ihsan"]

# 1) Basic slice (index 1 se 4 tak, 4 exclusive)
print(studentNames[1:4])  # ['Bilal', 'Usman', 'Sana']

# 2) Start se middle tak
print(studentNames[:3])   # ['Ahsan', 'Bilal', 'Usman']

# 3) Middle se end tak
print(studentNames[3:])   # ['Sana', 'Hina', 'Shahzad', 'Ihsan']

# 4) Step ke sath (har 2nd element)
print(studentNames[0:6:2]) # ['Ahsan', 'Usman', 'Hina']

# 5) Negative indexing (last 3 elements)
print(studentNames[-3:])  # ['Hina', 'Shahzad', 'Ihsan']








