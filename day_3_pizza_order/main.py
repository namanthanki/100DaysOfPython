print("Order Your Pizza!")
print("Small Pizza:\t$15\nMedium Pizza: \t$20\nLarge Pizza: \t$25\n")
print("Pepperoni for Small Pizza: \t\t+$2")
print("Pepperoni for Medium or Large Pizza: \t+$3\n")
print("Extra Cheese for any Pizza: \t+$1\n")

while True: 
    pizza_size = input("What size pizza do you want? S/s, M/m or L/l: ")
    if(
        pizza_size == 'S' or 
        pizza_size == 's' or 
        pizza_size == 'M' or 
        pizza_size == 'm' or 
        pizza_size == 'L' or 
        pizza_size == 'l'
    ):
        break
    else: 
        print("Please choose any correct option!")

while True:
    add_pepperoni = input("Do you want Pepperoni? Y/y or N/n: ")
    if(
        add_pepperoni == 'Y' or
        add_pepperoni == 'y' or
        add_pepperoni == 'N' or 
        add_pepperoni == 'n'
    ): 
        break
    else: 
        print("Please choose any correct option!")


while True:
    extra_cheese = input("Do you want extra cheese? Y/y or N/n: ")
    if(
        extra_cheese == 'Y' or
        extra_cheese == 'y' or
        extra_cheese == 'N' or 
        extra_cheese == 'n'
    ): 
        break
    else: 
        print("Please choose any correct option!")

final_bill = -1

if(pizza_size == 'S' or pizza_size == 's'):
    final_bill = 15
elif(pizza_size == 'M' or pizza_size == 'm'):
    final_bill = 20
else:
    final_bill = 25

if(add_pepperoni == 'Y' or add_pepperoni == 'y'):
    if(pizza_size == 'S' or pizza_size == 's'):
        final_bill += 2
    else:
        final_bill += 3

if(extra_cheese == 'Y' or extra_cheese == 'y'):
    final_bill += 1

print(f"Your Final Bill is ${final_bill}")