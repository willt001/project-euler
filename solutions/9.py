for a in range(500):
    for b in range(500):
        if 1000*a+1000*b-a*b==500000:
            print(a*b*(1000-a-b), a, b, 1000-a-b)
            break
    
