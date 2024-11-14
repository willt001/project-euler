import numpy as np

with open('solutions/problem11.txt', 'r') as num_file:
    nums = num_file.read()
    nums = nums.split()
    nums = np.array(list(map(int, nums))).reshape((20,20))
    nums2 = [nums[20*i: 20*i + 20] for i in range(20)]
    
greatest = 0
#horizontal
for i in range(20):
    for j in range(17):
        product = np.prod(nums[i][j:j+4])
        if product > greatest:
            greatest = product
#vertical
for i in range(20):
    for j in range(17):
        numst = np.transpose(nums)
        product = np.prod(numst[i][j:j+4])
        if product > greatest:
            greatest = product
#+diag
for i in range(3, 20):
    for j in range(17):
        product = nums[i][j]*nums[i-1][j+1]*nums[i-2][j+2]*nums[i-3][j+3]
        if product > greatest:
            greatest = product 
#-diag
for i in range(17):
    for j in range(17):
        product = nums[i][j]*nums[i+1][j+1]*nums[i+2][j+2]*nums[i+3][j+3]
        if product > greatest:
            greatest = product 
print(greatest)