N = int(input())

# for i in range(N-1):
result = []
a, b, c, d = map(int, input().split())
lst1 = [(x, y) for x in range(a, a+c) for y in range(b, b+d)]

for j in range(1, N):
    e, f, g, h = map(int, input().split())
    lst2 = [(x, y) for x in range(e, e+g) for y in range(f, f+h)]

    result = len([x for x in lst1 if x not in lst2])
    print(result)
print(len(lst2))

# result = []
# num_list = []
# alpha = ['a', 'b', 'c', 'd']
# for i in range(N):
#     num_list.append(input().split())

# # print(num_list)
    
#     lst1 = {}
#     for j in range(4):
#         lst1[alpha[j]] = num_list[i][j]
#     result.append(lst1)
# print(result)

# for i in range(N):
