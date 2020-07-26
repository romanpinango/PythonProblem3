# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

x = 13195
f = 0

for i in range(1,x):
    if x % i == 0 and isPrime(i):
        f = i

print(f)
