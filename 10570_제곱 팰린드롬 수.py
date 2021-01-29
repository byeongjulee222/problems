import sys; sys.stdin=open('txt/10570_제곱 팰린드롬 수.txt', 'r')

def check(num):
    num = str(num)
    flag = True
    Len = len(num)
    for i in range(Len//2):
        if num[i] != num[Len-i-1]:
            flag = False
            return flag
    return flag

def check_2(num):
    global cnt
    num = str(num)
    flag = True
    Len = len(num)
    print('num, Len', num, Len)
    print(type(num), num)
    for i in range(Len//2):
        if num[i] != num[Len-i-1]:
            flag = False
            return
    if flag == True:
        cnt += 1
        return


for tc in range(int(input())):
    A, B = map(int, input().split())
    cnt = 0
    Range = list(range(A, B+1))
    print(3//2)
    for num in Range:
        print(check(num))
        print('num**0.5 in Range', num**0.5 in Range)
        if check(num) and num**0.5 in Range:
            check_2(int(num**0.5))


    print('#{} {}'.format(tc+1, cnt))