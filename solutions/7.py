import numpy as np


sieve = [1] * 999999
sieve[0] = 0
sieve[1] = 0
for i, flag in enumerate(sieve):
    if flag==1:
        for j in range(i*i, 999999, i):
            sieve[j] = 0

primes = []
for i, flag in enumerate(sieve):
    if flag==1:
        primes.append(i)

print(primes[10000])