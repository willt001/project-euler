digits = list('0123456789')

from itertools import permutations

def has_property(A):
    if A[0]=='0':
        return False
    elif A[3] not in ['0', '2', '4', '6', '8']:
        return False
    elif A[5] not in ['0', '5']:
        return False
    else:
        return (int(A[1:4])%2 == 0) and (int(A[2:5])%3 == 0) and (int(A[3:6])%5 == 0) and (int(A[4:7])%7 == 0) and (int(A[5:8])%11 == 0) and (int(A[6:9])%13 == 0) and (int(A[7:10])%17 == 0)

perms = list(permutations(digits))
perms = [''.join(i) for i in perms]

total = 0
for perm in perms:
    if has_property(perm):
        total+=int(perm)
        print(perm)

print(total)