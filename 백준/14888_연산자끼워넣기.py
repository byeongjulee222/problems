op = '+-*/'
cnt = [2, 0, 1, 1]
N = 4
order = []

def backtrack(k):
    if k == N:
        print(*order)
    else:
        for i in range(4):
            if cnt[i]:
                cnt[i] -= 1
                order.append(op[i])
                backtrack(k+1)
                cnt[i] += 1
                order.pop()

backtrack(0)