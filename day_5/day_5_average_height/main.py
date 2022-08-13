print("Finding Average Height of Students\n")

students_height = input("Enter Student Heights(cm) Seperated by Spaces: ").split()
length = len(students_height)
sum = 0

for i in range(0, length):
    try: 
        students_height[i] = float(students_height[i])
    except: 
        print("Given Input is invalid")
        print("Hint: Try Something like: 160 165 180 155.5 140.5")
        exit()
    finally: 
        sum += students_height[i] 

average = sum / length

print(f"The average height of the Students: {average}")