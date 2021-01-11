import sys; sys.stdin = open('txt/17425_약수의 합.txt', 'r')

ans = [0 for _ in range(1000001)]

for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        ans[j] += i
    ans[i] += ans[i-1]

for i in range(int(input())):
    print(ans[int(input())])


'''
def func(n):
    if n == 1:
        sum_list[1] = 1
    elif n == 2:
        sum_list[2] = 4
    else:
        # Sum: 숫자 n의 약수의 합
        Sum = sum_list[n-1]
        for j in range(2, n):
            if n%j == 0:
                Sum += j
        sum_list[n] = Sum
    return

for tc in range(int(input())):
    num = int(input())
    sum_list = [0 for i in range(100001)]
    func(num)
    print(sum_list)
    print(sum_list[num])
'''