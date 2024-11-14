total = 0
for i in range(2, 5*(9**5)+1):
    nums = [int(char) for char in str(i)]
    if sum([num**5 for num in nums]) == i:
        print(i)
        total += i
print(total)