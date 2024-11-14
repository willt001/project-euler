def factorial_digit_sum(x):
    from math import factorial
    return sum([factorial(int(i)) for i in str(x)])

total=0

for i in range(3, 1000000):
    if i==factorial_digit_sum(i):
        total+=i

print(total)