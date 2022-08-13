print("Finding the Highest Score\n")

student_scores = input("Enter Student Scores Seperated by Space: ").split()
length = len(student_scores)

max = float('-inf')

for i in range(0, length):
    try: 
        student_scores[i] = float(student_scores[i])
    except: 
        print("Given Input is invalid")
        print("Hint: Try Something like: 16 65 80 55.5 ")
        exit()
    finally: 
        if student_scores[i] > max:
            max = student_scores[i]

print(f"Maximum Score: {max}")