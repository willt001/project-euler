import numpy as np

natural_numbers = np.array(range(101))
square_of_sum = np.sum(natural_numbers)**2
sum_of_squares = np.sum(natural_numbers**2)
print(sum_of_squares - square_of_sum)