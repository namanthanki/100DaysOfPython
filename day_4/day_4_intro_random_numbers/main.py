import random                               #psuedo random generator module (PRNG)

random_integer = random.randint(1, 10)      #generates random value in range of (start, end) 
random_float = random.random()              #generates random value between 0.00 and 0.99
random_float = random.random() * 10         #increasing range just by multiplying 

print(random_integer)
print(random_float)