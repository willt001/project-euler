primes = [1]*1000000
primes[0], primes[1] = 0, 0

for i in range(1000000):
    if primes[i]==1:
        for j in range(2*i, 1000000, i):
            primes[j]=0

def truncations(x):
    A = str(x)
    n = len(A)
    res = [x]
    for i in range(1, n):
        res.append(int(A[i:]))
        res.append(int(A[:n-i]))
    return res

total=0
for prime, is_prime in enumerate(primes):
    if is_prime==1:
        truncs = truncations(prime)
        if all([primes[trunc]==1 for trunc in truncs]) and prime>10:
            print(prime)
            total+=prime

print(total)