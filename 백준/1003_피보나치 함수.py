import sys; sys.stdin = open('txt/1003_피보나치 함수.txt', 'r')

def fibo(n):
    if n == 0 or n == 1:
        return
    else:
        for i in range(2, n+1):
            fibo_list[i][0] = fibo_list[i-1][0] + fibo_list[i-2][0]
            fibo_list[i][1] = fibo_list[i-1][1] + fibo_list[i-2][1]
        return


for i in range(int(input())):
    fibo_list = [[1, 0], [0, 1]] + [[0, 0] for _ in range(39)]
    n = int(input())
    fibo(n)
    print(fibo_list[n][0], fibo_list[n][1])