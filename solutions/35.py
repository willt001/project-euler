circularprimes = set()
primes = [1]*1000000
primes[0], primes[1] = 0, 0

for i in range(1000000):
    if primes[i]==1:
        for j in range(2*i, 1000000, i):
            primes[j]=0

def rotations(x):
    old = str(x)
    res = [int(x)]
    if len(old)==1:
        return res
    new = old[1:] + old[0]
    while new != old:
        res.append(int(new))
        new = new[1:] + new[0]
    return res

print(rotations(1))
    
for prime, is_prime in enumerate(primes):
    if is_prime==1:
        rots = rotations(prime)
        if all([primes[rot]==1 for rot in rots]):
            circularprimes.add(prime)
            print(prime)

print(len(circularprimes))