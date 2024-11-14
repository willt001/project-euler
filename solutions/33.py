def simplify(n, d):
    num, den = str(n), str(d)
    if "0" in num or "0" in den:
        return n, d
    for char in num:
        if char in den:
            num = num.replace(char, "", 1)
            den = den.replace(char, "", 1)
            return int(num), int(den)
    return n, d    


a, b = 1, 1
for d in range(10, 100):
    for n in range(10, d):
        num, den = simplify(n, d)
        if num != n and num/den == n/d:
            a *= num
            b *= den
print(a, b)