import sys; sys.stdin = open('txt/3079_입국심사.txt', 'r')

# 파라메트릭 서치 알고리즘 적용
# https://sarah950716.tistory.com/16
for _ in range(int(input())):
    # N: 심사대 개수, M: 사람 수
    N, M = map(int, input().split())
    inspect = []
    for _ in range(N):
        inspect.append(int(input()))

    left = 0
    right = M * max(inspect)
    while left <= right:
        mid = (left+right) // 2

        passed = 0
        for time in inspect:
            passed += mid // time

        if passed < M:
            left = mid + 1
        else:
            right = mid - 1

    print(right+1)