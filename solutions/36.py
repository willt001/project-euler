total = 0

for i in range(1000000):
    binary = bin(i)[2:]
    if str(i)==str(i)[::-1] and binary==binary[::-1]:
        print(i, binary)
        total+=i
print(total)