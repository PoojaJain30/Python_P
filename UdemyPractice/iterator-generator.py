###Problem 1 Create a generator that generates the squares of numbers up to some number N
def gensquares(N):
    for x in range(0,N):
        yield x**2 
    
for x in gensquares(10):
    print(x)


####Problem 2 Create a generator that yields "n" random numbers between a low and high number (that are inputs). Note: Use the random library. For example:

import random
def rand_num(low,high,n):
    for x in range(n):
        yield random.randint(low,high)
 

for num in rand_num(1,10,12):
    print(num)


####Problem 3 Use the iter() function to convert the string below into an iterator:
s = 'hello'
s_t = iter(s)
next(s_t)