x = 1
y = 2
total = 0
while x < 4000000:
    if x % 2 == 0:
        total += x
    x, y = y, x + y
    
print(total)