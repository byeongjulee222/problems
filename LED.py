import sys; sys.stdin = open("LED.txt", "r")

T = int(input())
# print(T)
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    numbers = [i for i in range(1, N+1)]
    # print(numbers)
    result = [[] for _ in range(1<<N)]
    # print(result)
    for i in range(1<<N):
        for j in range(N):
            if i & (1<<j):
                result[i].append(numbers[j])
    # print(result)
    final = []
    for set in result:
        for i in set:
            for room in range(1, len(arr)+1):
                if room % i == 0:
                    if arr[room-1] == 1:
                        arr[room-1] = 0
                    elif arr[room-1] == 0:
                        arr[room-1] = 1
            if 1 not in arr:
                final.append(len(set))
    print(final)