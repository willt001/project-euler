dic = {}

def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

dic[1] = 1
for i in range(2, 1000001):
    steps = 1
    j = i
    while j != 1:
        j = collatz(j)
        if dic.get(j):
            steps += dic.get(j)
            j = 1
        else:
            steps += 1
    dic[i] = steps
greatest = 1
greatest_idx = 1
for key, value in dic.items():
    if value > greatest:
        greatest = value
        greatest_idx = key

print(greatest_idx, greatest)
