def sum_of_evens(start, end): 
    if start % 2 != 0:
        start += 1
    
    end += 1

    sum = 0
    for number in range(start, end, 2): 
        sum += number

    print(f"Sum of all Evens from {start - 1} to {end - 1} = {sum}")


print("Adding Even Numbers in Range of x to y\n")

sum_of_evens(1, 100)
sum_of_evens(1, 500)
sum_of_evens(1, 1000)
