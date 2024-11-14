with open('51to100/problem67.txt') as num_file:
    f = num_file.read()
    triangle = []
    for line in f.split('\n'):
        triangle.append(list(map(int, line.split())))
    triangle.pop()

no_rows = len(triangle)
for i in range(no_rows - 2, -1 , -1):
    current_row = triangle[i]
    prev_row = triangle[i + 1]
    for j in range(len(current_row)):
        current_row[j] += max(
            prev_row[j],
            prev_row[j + 1]
        )

print(triangle[0][0])




    