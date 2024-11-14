with open('solutions/problem13.txt') as num_file:
    num_list = num_file.read().split('\n')
    num_list12 = [int(num[:12]) for num in num_list]
    num_list13 = [int(num[:13]) for num in num_list]
    num_list14 = [int(num[:14]) for num in num_list]

print(sum(num_list12), sum(num_list13),sum(num_list14))