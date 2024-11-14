def repeating_pattern(a, b):
    q = a//b
    r = a%b
    i = 1
    res = ''
    seen = [[q, r]]
    flag = 0
    while r > 0 and flag==0:
        q = (10*r)//b
        r = (10*r)%b
        if [q, r] in seen:
            flag=1
            seen.append([q, r])
        else:
            seen.append([q, r])
            res += str(q)
        i+=1
    
    return seen

def solution():
    most = 0
    for i in range(1, 1000):
        pattern = repeating_pattern(1, i)
        try:
            first = pattern.index(pattern[-1], 0, len(pattern)-1)
            repeat = len(pattern) - first - 1
        except:
            repeat = -1
        if repeat > most:
            most = repeat
            print(i, most)

solution()

