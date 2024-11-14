sieve = [True]*10000
sieve[0], sieve[1] = False, False
for i in range(10000):
    if sieve[i]:
        for j in range(2*i, 10000, i):
            sieve[j]=False
#print(sieve)

for i in range(1000, 10000):
    for j in range(1, (10000-i)//2):
        one = sorted(list(str(i)))
        two = sorted(list(str(i+j)))
        three = sorted(list(str(i+2*j)))
        if one==two and two==three and sieve[i] and sieve[i+j] and sieve[i+2*j]:
            print(i, i+j, i+2*j)