import sys
sys.stdin = open("zigzag.txt", "r")

TC = int(input())

for repeat in range(TC):
    number = int(input())

    result = 0
    for num in range(1, number+1):
        if num % 2:
            result += num
        else:
            result -= num

    print('#{} {}'.format(repeat+1, result))