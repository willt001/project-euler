onetonine = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
seen = set()

print(onetonine)

for a in range(1,9999):
    for b in range(1,99):
        c = a*b
        digits = list(str(a) + str(b) + str(c))
        if len(digits)==9 and set(digits)==onetonine:
            seen.add(c)
            print(a, b, c)

print(sum(list(seen)))