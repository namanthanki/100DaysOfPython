import random

print("Delicious Food Right?")
print("Alight then! it's time to pay the bill now\n")

names = input("Everyone!, give me your names (seperated by commas): ")

names = names.replace(" ", "")

if not names:
    print("Invalid Input")
    exit()

names = names.split(",")

length = len(names)

if length == 1:
    bill_payer = names[0]
else:
    bill_payer = names[random.randint(0, length - 1)]
print(f"{bill_payer} will pay this time for all the Delicious Food!")