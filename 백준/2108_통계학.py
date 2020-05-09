import sys; sys.stdin = open('txt/2108_통계학.txt', 'r')
from collections import Counter

for _ in range(int(input())):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(int(input()))

    # 이 부분에서 sum(arr)//N으로 했다가 틀렸음
    print(round(sum(arr) / N))

    arr.sort()
    print(arr[N // 2])

    # collections.Counter
    # 리스트 안에 있는 요소들의 개수를 dict 형태로 반환해줌
    cnt = Counter(arr)

    # sorted(정렬할 요소, key=lambda x: (첫번째 정렬 기준, 두번째 정렬 기준))
    # 개수 많은 순서로 내림차순 + 작은 값부터 오름차순
    cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
    if len(cnt) > 1:
        if cnt[0][1] == cnt[1][1]:
            print(cnt[1][0])
        else:
            print(cnt[0][0])
    else:
        print(cnt[0][0])

    print(arr[-1] - arr[0])