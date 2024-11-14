primes = [True]*1000000
primes[0]=False
primes[1]=False

for i in range(1000000):
    if primes[i]:
        for j in range(2*i, 1000000, i):
            primes[j]=False

primeList = []
for prime, isPrime in enumerate(primes):
    if isPrime:
        primeList.append(prime)

twiceSquaresSet = set([2*(i**2) for i in range(1, 1000)])
sieve = primes

def solution(sieve, squares):
    greatest = 1
    for odd in range(9, 1000000, 2):
        if sieve[odd]:
            continue
        i = odd-2
        while i>1:
            if not sieve[i]:
                i-=1
                continue
            if odd-i in squares:
                print(odd, i, odd-i)
                greatest = odd
                i=1
            i-=1
        if odd>greatest:
            return odd
        
print(solution(sieve, twiceSquaresSet))