import sys; sys.stdin = open("txt/1976_time_sum.txt", "r")

T = int(input())
for tc in range(1, T+1):
    t1, m1, t2, m2 = map(int, input().split())

    result = (t1 + t2) * 60 + (m1 + m2)
    # print(result)
    time, minute = result // 60, result % 60
    if time > 12:
        time -= 12
    print('#{} {} {}'.format(tc, time, minute))
