# Car ki dictionary banani
carInfo = {
    "brand": "Toyota",       # Car ka brand name
    "model": "Corolla",      # Car ka model name
    "year": 2020,            # Car ka model year
    "color": "White",        # Car ka rang
    "isElectric": False,     # Kya car electric hai? (True/False)
    "features": ["AC", "ABS", "Airbags"],  # Car ki features ki list
    "price": 3500000,        # Car ki price PKR me
    "owner": {               # Nested dictionary (Owner ki info)
        "name": "Ali",       # Owner ka naam
        "city": "Lahore",    # Owner ka city
        "phone": "0300-1234567"  # Owner ka phone number
    }
}

# Dictionary ka data access karna
print("Car Brand:", carInfo["brand"])      # Brand print karega
print("Car Model:", carInfo["model"])      # Model print karega
print("Car Year:", carInfo["year"])        # Year print karega
print("Car Color:", carInfo["color"])      # Color print karega
print("Electric Car?", carInfo["isElectric"])  # Electric status print karega
print("Car Features:", carInfo["features"])    # Features list print karega
print("Car Price:", carInfo["price"], "PKR")   # Price print karega
print("Owner Name:", carInfo["owner"]["name"]) # Nested dictionary ka data print karega

# Dictionary me naya key add karna
carInfo["registrationNo"] = "LEA-1234"  # Roman Urdu: Naya key add kiya

# Dictionary me value change karna
carInfo["color"] = "Black"  # Roman Urdu: Car ka color update kar diya

# Dictionary me se key delete karna
del carInfo["isElectric"]  # Roman Urdu: Electric info delete kar di

# Updated dictionary print karna
print("\nUpdated Car Info:", carInfo)
