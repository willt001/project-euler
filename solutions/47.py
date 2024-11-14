n=1000000
sieve = [True]*n
sieve[0]=False
sieve[1]=False

for i in range(2, n):
    if sieve[i]:
        for j in range(2*i, n, i):
            sieve[j]=False

def primeFactors(x):
    factors = []
    i = 2
    while i<=x**0.5 + 1:
        if not sieve[i]:
            i+=1
            continue
        if x%i==0:
            factors.append(i)
            while x%i==0:
                if sieve[x//i] and x//i not in factors:
                    factors.append(x//i)
                x = x//i
        i+=1
    return factors

def solution():
    memory = [primeFactors(i) for i in range(2, 6)]
    for i in range(1000000):
        one, two, three, four = memory[i], memory[i+1], memory[i+2], memory[i+3]
        if len(one)>=4 and len(two)>=4 and len(three)>=4 and len(four)>=4:
            return i, one, two, three, four
        memory.append(primeFactors(i+4))
    return -1
print(solution())