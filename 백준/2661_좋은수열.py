def backtrack(idx):
    # 끝에서 부터 1개, 2개, ...i개씩 비교
    for i in range(1, (idx//2) + 1):
        if num[-i:] == num[2 * (-i):-i]:
            return -1

    # 종료조건
    if idx == n:
        for i in range(n):
            print(num[i], end='')

        # return 0을 해서 함수를 끝낼 수 있도록 함
        return 0

    # 작은수부터 차례대로 맨 끝에 붙여보고
    # 좋은 수열인지 판단
    for i in range(1, 4):
        num.append(i)
        if backtrack(idx + 1) == 0:
            return 0

        # return 이 -1이면 좋은수열이 아님
        num.pop()

n = int(input())
num = []
backtrack(0)