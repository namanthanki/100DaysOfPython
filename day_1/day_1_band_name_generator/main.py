#-> Day-1-Challenge: Band Name Generator
#-> Requirements: 
#   -Greet User
#   -Ask for user's city
#   -Ask for user's pet name
#   -Combine these two and display 

print("Welcome to Band Name Generator!!!\n")

user_city = input("What city did you grow up in?\n")
user_pet = input("\nWhat is your pet's name?\n")

band_name = user_city + ' ' + user_pet

print("\nYour Band Name is: " + band_name)