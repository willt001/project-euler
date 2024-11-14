total = 0
for i in range(1, 1001):
    total+= (i**i)%10000000000
print(str(total))