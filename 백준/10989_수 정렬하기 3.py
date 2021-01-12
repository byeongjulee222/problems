import sys; sys.stdin = open('txt/10989_수 정렬하기 3.txt', 'r')

num_list = [0 for _ in range(10001)]
for _ in range(int(input())):
    num_list[int(sys.stdin.readline())] += 1

for num in range(10001):
    if num_list[num]:
        for _ in range(num_list[num]):
            print(num)
