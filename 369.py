import sys
sys.stdin = open("369.txt", "r")
N = int(input())

num_list = list(map(str, range(1,N+1)))
result = []
for num in num_list:
    result += [list(num)]
# print(result)

for i in result:
    if '3' in i:
        i[i.index('3')] = '-'
    if '6' in i:
        i[i.index('6')] = '-'
    if '9' in i:
        i[i.index('9')] = '-'

for i in result:
    if '3' in i:
        i[i.index('3')] = '-'
    if '6' in i:
        i[i.index('6')] = '-'
    if '9' in i:
        i[i.index('9')] = '-'
      
final = ''
for j in result:
    final += ''.join(j) + ' '
print(final, end='')    
# print(' '.join(result))