import sys
sys.stdin = open("pascal_triangle.txt", "r")

TC = int(input())

num_list = [[]] * 10
for i in range(TC):
    numbers = int(input())
    if i == 0:
        num_list[i].append(1)
        print(num_list)
    # else:
    #     for j in range(numbers):
    #         if j == 0 or j == numbers-1:
    #             num_list += [1]
    #     print(num_list)
            # else:
            #     num_list[i][j] == num_list[i-1][]
    # print(num_list)


    # for i in range(1, numbers+1):
    #     print('#{}'.format(repeat+1))
    #     if i == 1:
    #         print(i)
    #     else:
    #         num_list[0] = num_list[-1] = 1
    #         for j in range(1, numbers-1):
    #             result[j] == result[j-1] +      