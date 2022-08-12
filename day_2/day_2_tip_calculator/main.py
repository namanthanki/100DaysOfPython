print("Welcome to the Tip Calculator\n")

bill = float(input("What is total bill?: "))
number_of_people = int(input("What is the number of people you want to split bill with?: "))
tip_percentage = 0

while True: 
    tip_percentage = int(input("What percentage of tip would you like to give? (10, 12 or 15): "))
    if tip_percentage == 10 or tip_percentage == 12 or tip_percentage == 15:
            break
    else: 
        print("Please enter valid tip percentage\n")

total_tip = bill * (tip_percentage / 100)
total_bill = bill + total_tip
bill_per_person = total_bill / number_of_people


print(f"Your final split per person would be: {round(bill_per_person, 2)}")
    
    
    

