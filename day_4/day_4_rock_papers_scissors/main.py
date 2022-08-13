import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Rock: \t  (1)\nPaper: \t  (2)\nScissors: (3)\n")
user_choice = int(input("Your call?: "))
choices = [ "Rock", "Paper", "Scissors" ]
choice_lookup = [ 1, 2, 3 ]
game_art = [ rock, paper, scissors ]

if user_choice not in choice_lookup: 
    print("Invalid Input, Please try values from 1, 2 or 3")
    exit()
else: 
    print(f"You chose     : {choices[user_choice - 1]}")
    print(game_art[user_choice - 1])

rand_index = random.randint(0, 2)
computer_choice = choices[rand_index]
print(f"Computer chose: {computer_choice}")
print(game_art[rand_index])

if choices[user_choice - 1] == computer_choice:
    print("It's a Draw!")
    exit()

if user_choice == 1 and computer_choice == choices[2]: 
    print("It's Your Victory!")
    exit()
if user_choice == 2 and computer_choice == choices[0]:
    print("It's Your Victory")
    exit()
if user_choice == 3 and computer_choice == choices[1]:
    print("It's Your Victory")
    exit()

print("Computer Wins!")