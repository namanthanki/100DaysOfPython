import random
import ascii_art
import words


print(ascii_art.logo)
stages = ascii_art.stages

word = random.choice(words.word_list)
has_won = False

print("Guess the Word: ")

length = len(word)
current_state = list()
for i in word: 
    current_state.append("_")

life = 6

while True:
    if life == 0: 
        print(stages[0])
        break
    print(" ".join(current_state));
    print(stages[life])
    if not "_" in current_state: 
        has_won = True
        break
    while True: 
        guessed_letter = input("Guess the Letter: ").lower()
        if(len(guessed_letter) == 1):
            break
        else:
            print("Please Only Input a Letter at Once...")

    if guessed_letter in word: 
        for i in range(length):
            if(guessed_letter == word[i]):
                current_state[i] = guessed_letter
    else: 
        print("Try Guessing Again...")
    life -= 1

print("You Won") if has_won else print("You Lost!")
