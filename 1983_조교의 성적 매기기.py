import sys; sys.stdin = open('txt/1983_조교의 성적 매기기.txt', 'r')

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = {}
    for i in range(1, N+1):
        arr, b, c = map(int, input().split())
        arr[i] = 35 * arr + 45 * b + 20 * c

    result = sorted(arr.items(), key=lambda x : x[1], reverse=True)
    # print(result)

    idx = 0
    for arr, b in result:
        if arr == K: res = idx
        idx += 1

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    # print(res)
    n = N//10
    # print(res//n)
    # print(grade[res//n])
    print('#{} {}'.format(tc, grade[res//n]))