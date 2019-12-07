# def isgood(arr):
#     compare = ''
#     # while len(compare) < N:
#     for i in arr:
#         compare += i
#         for j in compare:
#             if compare[:j] ==



# N = int(input())
arr = ['1', '2', '3']
word = ''


def isgood(word):
    cnt = 0
    for i in range(len(word)):
        for j in range(i, len(word)):
            if word[i:j] == word[j:2*j-i]:
                continue
    return True

print(isgood('121'))




# def perm(k, n):
#     global M
#     if k == M:
#         print(order.join())
#         return
#
#     for i in range(1, N+1):
#         order.append(i)
#         perm(k+1, n)
#         order.pop()
#
# order = []
# N, M = map(int, input().split())
# visit = [0] * (N+1)
# perm(0, N)