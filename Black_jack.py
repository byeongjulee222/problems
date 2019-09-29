# def black_jack(k, s):
#     global result
#     if sum(choose) > M:
#         return
#
#     if k == 3 and result < sum(choose):
#         result = sum(choose)
#         return result
#
#     for i in range(s, N):
#         choose.append(arr[i])
#         black_jack(k+1, i+1)
#         choose.pop()
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# choose = []
# result = 0
# black_jack(0, 0)
# print(result)
# 5 6 7 8 9

def black_jack(num, select, calc):
    global res

    if calc > M: return

    if select >= len(arr): return

    if num > 3: return

    if num == 3:
        res = max(res, calc)
        return

    black_jack(num + 1, select + 1, calc + arr[select])
    black_jack(num, select + 1, calc)

N, M = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
black_jack(0, 0, 0)
print(res)