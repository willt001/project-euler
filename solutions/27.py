def quadratic(x, a, b):
    return x**2 + a*x + b

def is_prime(x):
    i = 3
    if x < 2:
        return False
    if x>2 and x%2==0:
        return False
    while i <= x**0.5:
        if x%i==0:
            return False
        i+=1
    return True

longest_chain = 0
for a in range(-1000, 1000):
    for b in range(-1000, 1001):
        n = 0
        while is_prime(quadratic(n, a, b)):
            n+=1
        if n > longest_chain:
            longest_chain = n
            solution = (a, b, a*b)
print(solution)