import math

x=math.factorial(100)

x = list(map(int, list(str(x))))

print(sum(x))