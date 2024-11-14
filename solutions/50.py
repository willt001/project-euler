sieve = [True]*1000000
primes = []
sieve[0], sieve[1] = False, False
for i in range(1000000):
    if sieve[i]:
        primes.append(i)
        for j in range(2*i, 1000000, i):
            sieve[j]=False

def solution(primes, sieve):
    result = -1
    for width in range(2, 1000):
        total = sum(primes[:width])
        for i in range(len(primes) - width):
            total -= primes[i]
            total += primes[i + width]
            if total < 1000000 and sieve[total]:
                result = total
    return result


print(solution(primes=primes, sieve=sieve))