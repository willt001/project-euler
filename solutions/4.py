def is_palindrome(x):
    x = str(x)
    i, j = 0, len(x) - 1
    while i < j:
        if x[i] == x[j]:
            i+=1
            j-=1
        else: 
            return False
    return True

max_palindrome = 1
for i in range(101,10000):
    for j in range(101,10000):
        if i*j > max_palindrome and is_palindrome(i*j):
            max_palindrome = i*j
            pair = i, j

print(max_palindrome, pair)