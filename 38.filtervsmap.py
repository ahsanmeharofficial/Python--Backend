# Difference between map() vs filter():

# 1. map() ka kaam:
#    - Har element par ek function lagata hai
#    - Har element ko modify karke nayi list banata hai
#    - Har element ka result list me hota hai (length same hoti hai)

# 2. filter() ka kaam:
#    - Sirf un elements ko rakhta hai jo condition ko pass karein
#    - List ke elements ki length kam ho sakti hai
#    - Elements ko modify nahi karta, bas select karta hai

# Short example:
# map() → [1, 2, 3] → double → [2, 4, 6]
# filter() → [1, 2, 3] → even select → [2]
