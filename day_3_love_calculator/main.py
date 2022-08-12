from time import thread_time_ns


print("Love Calculator\n\n")

your_name = input("What is Your Name: ")
their_name = input("What is Their Name: ")

names = your_name + their_name
names = names.lower()

t = names.count('t')
r = names.count('r')
u = names.count('u')
e = names.count('e')

true = t + r + u + e

l = names.count('l')
o = names.count('o')
v = names.count('v')
e = names.count('e')

love = l + o + v + e

true_love = int(str(true) + str(love))
if(true_love < 10 or true_love > 90):
    print(f"Your Score is {true_love}%, you go together like coke and mentos")
elif(true_love >= 40 and true_love <= 50):
    print(f"Your Score is {true_love}%, you are alright together")
else:
    print(f"Your Score is {true_love}%")
