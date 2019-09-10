import sys; sys.stdin = open("txt/1970_easy_change.txt", "r")

T = int(input())
for tc in range(1, T+1):
    change = int(input())
    list = [0 for _ in range(8)]
    # print(list)

    if change // 50000:
        list[0] += change//50000
        change -= 50000 * (change//50000)
    if change // 10000:
        list[1] += change//10000
        change -= 10000 * (change//10000)
    if change // 5000:
        list[2] += change//5000
        change -= 5000 * (change//5000)
    if change // 1000:
        list[3] += change//1000
        change -= 1000 * (change//1000)
    if change // 500:
        list[4] += change//500
        change -= 500 * (change//500)
    if change // 100:
        list[5] += change//100
        change -= 100 * (change//100)
    if change // 50:
        list[6] += change//50
        change -= 50 * (change//50)
    if change // 10:
        list[7] += change//10
        change -= 10 * (change//10)
    print('#{}'.format(tc), end='\n')
    print(*list)