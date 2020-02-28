import sys; sys.stdin = open('txt/1952_수영장.txt', 'r')

def swim(price, date):
    global Min
    if date >= 12:
        Min = min(Min, price)
        return

    # 해당하는 달에 이용 계획이 없으면 다음달로 넘어감
    if not schedule[date]:
        swim(price, date+1)

    # 이용 계획이 있는 경우 백트래킹 진행
    else:
        swim(price + day*schedule[date], date+1)
        swim(price + month, date+1)
        swim(price + month_3, date+3)

for tc in range(1, int(input())+1):
    day, month, month_3, year = list(map(int, input().split()))
    schedule = list(map(int, input().split()))

    # 일년치 결제하는 것보다 더 많이 나올 수 없음
    Min = year
    swim(0, 0)

    print('#{} {}'.format(tc, Min))