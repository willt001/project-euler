def count_divisors(n):
    res = 0 
    i = 1               
    while i**2 < n:
        if n%i==0:
            res+=2
        i+=1
    if i**2==n:
        res+=1
    return res

i = 1   
while True:
    t = i*(i+1)/2
    if count_divisors(t) > 500:
        print(t, count_divisors(t))
        break
    i+=1