found = 0
i=2
pentagonals = set()
hexagonals = set()

while found < 2:
    pentagonals.add(int(i*(3*i - 1)/2))
    hexagonals.add(int(i*(2*i - 1)))
    triangle = int(i*(i+1)/2)
    if (triangle in pentagonals) and (triangle in hexagonals):
        found+=1
        print(i, triangle)
    i+=1