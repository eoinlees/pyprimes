# Eoin Lees
# Computing the primes.

from functions import isprime

# My list of Primes - TBD
P = []

# Loop through all of the numbers we're checking for Primality.
for i in range(2,100):
   
    # If i is prime, then append to P.
    if isprime(i):
        P.append(i)

# Print out our list
print(P)
