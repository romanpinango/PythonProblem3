# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# A better approach:
# We need to divide the number by the lowest possible prime number,
# as many times as we need to reduce it to 1

# Let's save primes in an array to improve performance
primes = [2]

# Function to calculate the next prime number after prime number p
def calculateNextPrime(p):
    isPrime = False
    while not isPrime:
        p += 1
        # Validate with precalculated primes
        isDivisible = False
        for j in range(len(primes)):
            if p % primes[j] == 0:
                isDivisible = True
                break
        if not isDivisible:
            primes.append(p)
            isPrime = True
    return p

# Funtion to find the next prime number after prime number p, if it was
# already calculated we just return it
def findNextPrime(p):
    for i in range(len(primes)):
        if primes[i] == p:
            if i+1 < len(primes):
                return primes[i+1]
            else:
                return calculateNextPrime(p)

# x is the number to factorize,
# f the max factor and
# p the current prime number
x = 600851475143
f = 0
p = 0

while x > 1:
    p = 2
    if x % p == 0:
        x = x // p
    else:
        isDivisible = False
        while not isDivisible:
            y = findNextPrime(p)
            if x % p == 0:
                isDivisible = True
                x = x // p
                f = p if p > f else f

print(f)
