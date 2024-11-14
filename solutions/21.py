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

counted = set()
for i in range(1, 10000):
    y = proper_divisor_sum(i)
    if proper_divisor_sum(y)==i and y!=i:
        counted.add(y)
        counted.add(i)

print(sum(counted))