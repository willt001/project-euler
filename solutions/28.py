n = 1
total = 1
multiple = 2
while multiple<1001:
    for _ in range(4):
        n += multiple
        total += n
    multiple += 2
print(total)