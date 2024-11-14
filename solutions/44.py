pentagonals = [int(i*(3*i - 1)/2) for i in range(1, 10000)]

p_set = set(pentagonals)

for i in pentagonals:
    for j in pentagonals:
        if (i+j in p_set) and (abs(i-j) in p_set) and (i!=j):
            print(i, j, i-j)

print()