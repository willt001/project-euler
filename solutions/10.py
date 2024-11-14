def solution():
    import numpy as np

    bound = 2000000
    sieve = np.ones(bound, dtype = 'longlong')
    sieve[0] = 0
    sieve[1] = 0
    for i, flag in enumerate(sieve):
        if flag==1:
            for j in range(2*i, bound, i):
                sieve[j] = 0
    for i, flag in enumerate(sieve):
        if flag==1:
            sieve[i] = i
    return np.sum(sieve)

print(solution())
