import decimal
decimal.getcontext().prec = 100

def fib(n):
    n = decimal.Decimal(n)
    phi = decimal.Decimal((1+(5**.5))/2)
    iphi = decimal.Decimal((1-(5**.5))/2)
    return (phi**n - iphi**n) / decimal.Decimal(5)**decimal.Decimal(.5)


bound = 10**999
i=1
while fib(i) < bound:
    i+=1
    
print(i, fib(i))
