# def recur(k, n):
#     global result
#     k += 1
#     if n == 1:
#         return 1
#     elif k == N+1:
#         return result
#     else:
#         result *= k
#         recur(k, n)
#
# N = int(input())
# result = 1
# recur(0, N)
# print(result)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

k = int(input())
print(fact(k))