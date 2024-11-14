import numpy as np

with open('solutions/problem8.txt', "r") as num_file:
    num = num_file.read()
    num = num.replace('\n', '')
    num = np.array(list(map(int, num)), dtype = 'longlong')

greatest = 0
for i in range(1000-13):
    product = np.prod(num[i:i+13])
    if product > greatest:
        greatest = product
print(num[i:i+13], greatest)
        

