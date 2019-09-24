import sys; sys.stdin = open("txt/BOJ_2580_sudoku.txt")

arr = [list(map(int, input().split())) for _ in range(9)]
# print(arr)

nine = [x for x in range(1, 10)]
num_list = nine
for row in arr:
    for i in row:
        if i in num_list:
            num_list.pop(num_list.index(i))
    if len(num_list) == 1 and


