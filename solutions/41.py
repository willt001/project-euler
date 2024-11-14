from itertools import permutations
# sum from 1 to n (n) = n(n+1)/2, the sum cannot be divisible by 3, therefore n = 1 mod 3
digits = list('1234567')

perms = permutations(digits)

perms = [int(''.join(perm)) for perm in list(perms)]

primes = [1]*10000000
primes[0], primes[1] = 0, 0
for i in range(10000000):
    if primes[i]==1:
        for j in range(2*i, 10000000, i):
            primes[j]=0

largest = 0
for perm in perms:
    if primes[perm]==1 and perm > largest:
        largest=perm
        print(largest)

print(largest)