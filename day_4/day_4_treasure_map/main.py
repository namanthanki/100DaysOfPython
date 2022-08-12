def print_map(): 
    a = 97
    for i in map:
        print(chr(a), i)
        a += 1

    print("     1     2     3")


row1 = ["⬜","⬜️","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

map = [row1, row2, row3]

print_map()

hide = input("where do you want to put your treasure? (Hint: try something like a2):  ")

alpha_lookup = { 'a': 0, 'b': 1, 'c': 2}

map[alpha_lookup[hide[0]]][int(hide[1]) - 1] = ' x'

print_map()

