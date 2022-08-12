import random

print("Delicious Food Right?")
print("Alight then! it's time to pay the bill now\n")

names = input("Everyone!, give me your names (seperated by commas): ")

names = names.replace(" ", "")
names = names.split(",")

bill_payer = names[random.randint(0, len(names) - 1)]

print(f"{bill_payer} will pay this time for all the Delicious Food!")