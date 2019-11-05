import sys; sys.stdin = open('txt/1946.txt', 'r')

for tc in range(1, int(input())+1):
    word = ''
    for i in range(int(input())):
        alpha, num = input().split()
        num = int(num)
        word += alpha*num
    print('#{}'.format(tc))
    for j in range(len(word)//10):
        print(word[10*j:10*(j+1)])
    print(word[len(word)//10*10:len(word)])