def f(p, a, b):
    return p**2 - 2*p*(a+b) + a*b

result, no = 0, 0
for p in range(12, 1001):
    current_no = 0
    for i in range(1, p//2):
        for j in range(1, p//2):
            if (f(p, i, j)==0):
                current_no+=1
    if current_no > no:
        result, no = p, current_no
print(result, no)

