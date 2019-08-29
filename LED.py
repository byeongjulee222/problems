import sys; sys.stdin = open("txt/LED.txt", "r")

T = int(input())
# print(T)
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    print(arr)

    cnt = 0
    for i in range(1, len(arr)):
        if arr[i] == 1:
            for j in range(1, len(arr)):
                if j % i == 0:
                    if arr[j] == 1:
                        arr[j] = 0
                    else:
                        arr[j] = 1
            cnt += 1
        else:
            continue
    print(cnt)







    # N = int(input())
    # arr = [0] + list(map(int, input().split()))
    # # arr = [0, 0, 0, 0, 0, 0, 1]
    # numbers = [i for i in range(1, N+1)]
    # # print(numbers)
    # result = [[] for _ in range(1<<N)]
    # # print(result)
    # for i in range(1<<N):
    #     for j in range(N):
    #         if i & (1<<j):
    #             result[i].append(numbers[j])
    # # print(result)
    # final = []
    # for set in result:
    #     for i in set:
    #         for room in range(1, len(arr)):
    #             if arr[room] == 1:
    #                 if room % i == 0:
    #                 # if arr[room] == 1:
    #                     arr[room] = 0
    #                 # elif arr[room] == 0:
    #                 #     arr[room] = 1
    #         if sum(arr) == 0:
    #             final.append(set)
    #
    # print(final)