import sys; sys.stdin = open('예산.txt')

def solution(d, budget):
    d.sort()
    Sum = sum(d)
    for i in range(len(d)-1, -1, -1):
        if Sum <= budget:
            return i + 1
        else:
            if i == 0: return 0
            Sum -= d[i]

for _ in range(int(input())):
    d = list(map(int, input().split()))
    budget = int(input())
    # print(d)
    print(solution(d, budget))