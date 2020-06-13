import sys; sys.stdin = open("txt/8016_pyramid.txt", "r")

def pyramid(num):
    if num == 1:
        return 1
    else:
        return pyramid(num-1) + 2 + 4*(num-2)

T = int(input())
for tc in range(1, T+1):
    print('#{} {} {}'.format(tc, pyramid(tc), pyramid(tc)+(4*(tc-1))))