def proper_divisor_sum(x):
    res = [1]
    i=2
    while i**2<x:
        if x%i==0:
            res.extend([i, x//i])
        i+=1
    if i**2==x:
        res.append(i)
    return sum(res)

abundant = []
for i in range(1, 28124):
    if i < proper_divisor_sum(i):
        abundant.append(i)
abundant_set = set(abundant)

can = set()
for i in range(1,28124):
    j = 0
    while abundant[j]<=i:
        if i - abundant[j] in abundant_set:
            can.add(i)
            print(i)
            break
        j+=1

print(sum(list(range(28124)))-sum(can))
