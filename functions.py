# Eoin Lees
# A function to square numbers. 

# () Whatever is in the brackets is called the arguments

import math

def power(x,y):
    ans = x
    y = y - 1
    while y > 0:
        ans = ans * x
        y = y - 1
    return ans

print(power(-10,-6))

def f(x):
    ans = (100 * power(x, 2) + 10 * power(x, 3)) // 100
    ans = ans - (power(x, 3) // 10)
    return ans

print(f(5))

#This picks out prime numbers in selected range.

def isprime(i):
    # Loop through all values j from 2 up to but not including i.
    for j in range(2, math.floor(math.sqrt(i))):
        # See if j divides i.
        if i % j == 0:
            # If it does, i isn't prime so exit the loop and indicate not prime.
            return False
    return True
