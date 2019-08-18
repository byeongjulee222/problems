S_num = int(input())
S_num_list = input().split()
C_num = int(input())
C_num_list = input().split()
# print(S_num_list, C_num_list)

result = ''
for num in C_num_list:
    if num in S_num_list:
        result += '1' + ' '
    else:
        result += '0' + ' '

print(result, end='')