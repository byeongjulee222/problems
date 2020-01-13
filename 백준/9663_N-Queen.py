# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하라

def nqueen(sol, n):
    global count
    if len(sol) == n:
        count += 1
        return

    candidate = list(range(n))
    for i in range(len(sol)):
        if sol[i] in candidate:
            candidate.remove(sol[i])
        dist = len(sol) - i
        if sol[i] + dist in candidate:
            candidate.remove(sol[i] + dist)
        if sol[i] - dist in candidate:
            candidate.remove(sol[i] - dist)

    if candidate != []:
        for i in candidate:
            sol.append(i)
            nqueen(sol, n)
            sol.pop()
    else: return

count = 0
num = int(input())
for i in range(num):
    nqueen([i], num)
print(count)
