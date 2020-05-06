N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    num = arr[0]
    lst = arr[1:]
    avg_score = sum(lst)//num
    cnt = 0
    for student in lst:
        if student > avg_score:
            cnt += 1
    ans = float(cnt/num*100)
    print('{0:0.3f}%'.format(ans))