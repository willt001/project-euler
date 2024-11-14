with open('22.txt') as my_file:
    names = my_file.read().replace('\n', '')
    names = names.replace('"', '')
    names = names.split(',')
    names.sort()

def name_score(name):
    return sum([ord(letter)-64 for letter in name])

total = 0
for i, name in enumerate(names, 1):
    total += i*name_score(name)

print(total)