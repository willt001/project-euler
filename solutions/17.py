
total = 0

def letter_count(x):
    res = 0
    dic = {0:0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7:5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13:8, 14:8, 15:7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30:6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}
    if x == 1000:
        res += 11
        return res
    elif x >= 100 and x%100==0:
        res += 7 + dic.get(x//100)
        return res
    elif x > 100:
        res += 10 + dic.get(x//100)
    y = x%100
    if y > 20:
        res += dic.get(y - y%10) + dic.get(y%10)
    else:
        res += dic.get(y)
    return res

print(sum([letter_count(i) for i in range(1,1001)]))