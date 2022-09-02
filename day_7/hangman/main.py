import random

word = "beekeeper"
has_won = False

print("Guess the Word: ")

length = len(word)
current_state = list()
for i in word: 
    current_state.append("_")

life = length + 1

while True:
    if life == 0: 
        break
    print(" ".join(current_state));
    if not "_" in current_state: 
        has_won = True
        break
    guessed_letter = input("Guess the Letter: ")

    if guessed_letter in word: 
        for i in range(length):
            if(guessed_letter == word[i]):
                current_state[i] = guessed_letter
    else: 
        print("Try Guessing Again...")
    life -= 1

print("You Won") if has_won else print("You Lost!")
