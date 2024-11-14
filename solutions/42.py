with open('1to50/42.txt') as my_file:
    words = my_file.read().replace('\n', '')
    words = words.replace('"', '')
    words = words.split(',')



def word_score(A):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    dic = {}
    for key, value in enumerate(alphabet):
        dic[value] = key+1
    
    res = 0
    for char in A:
        res += dic.get(char)
    
    return res

result = 0

triangles = set([i*(i+1)/2 for i in range(1000)])

for word in words:
    score = word_score(word)
    if score in triangles:
        result+=1

print(result)
