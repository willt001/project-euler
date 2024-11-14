digits = list('123456789')

def pan_product(x,n):
    res = ''
    for i in range(1, n+1):
        res += str(x*i)
    return res

largest = 0

for i in range(1, 10000):
    for j in range(2, 9):
        prod = pan_product(i, j)
        if (sorted(list(prod))==digits) and int(prod)>largest:
            largest = int(prod)
            print(largest, i, j)
