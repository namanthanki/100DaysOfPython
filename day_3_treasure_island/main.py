print("Welcome to the Treasure Island\n")
print("Your Mission is to Find Treasure\n")

game_over = False

while game_over == False:
    path = input("left or right")
    if(path == "right"):
        game_over = True
        break
    else: 
        swim_or_wait = input("swim or wait")
        if(swim_or_wait == "swim"):
            game_over = True
            break
        else:
            door = input("Which door (Red, Blue or Yellow): ")
            if(door == "red" or door == "blue"):
                game_over = True
                break
            else: 
                print("You win")
                break
