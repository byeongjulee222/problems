import sys; sys.stdin = open('txt/1110_더하기 사이클.txt', 'r')

for _ in range(int(input())):
    num = input()
    if len(num) == 1:
        num = '0' + num
    new_num = num
    cnt = 0
    while True:
        # print(num)
        new_num = new_num[-1] + str(int(new_num[0]) + int(new_num[1]))[-1]
        cnt += 1
        if num == new_num: break
        # print(num, new_num)
    # print(new_num)
    print(cnt)