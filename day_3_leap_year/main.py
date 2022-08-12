print("Check Whether a Year is Leap Year or not\n\n")

year = int(input("Enter Year: "))

if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a Leap Year")
else:   
    print(f"{year} is not a Leap Year")