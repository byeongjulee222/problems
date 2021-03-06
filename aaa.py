# from itertools import permutations
#
#
# a = list(permutations([2, 3]))
# print(a)
#
# # 1 2 3
# #
# # 1 2 3 1
# # 1 3 2 1
#
#
# arr = [[(j, i) for i in range(1, 4)] for j in range(1, 4)]
# print(arr)
#
#
# a = 5
# while a:
#     print(a)
#     a -= 1
# print('over')

'''
def getMin(문제크기):
    if 가장 작은 문제

    else:
        getMin(더 작은 문제)

print(getMin(원문제의 크기))
'''


# arr = [9, 2, 3, 7, 5, 6, 8, 1, 4, 10]
#
# def getMin(s, e):   # 최소값 구하기
#     if s == e:      # 기저 사례
#         return arr[s]
#
#     else:
#         ret = getMin(s, e-1)
#         return min(ret, arr[e])
#
#         # 분할 탐색
#         # mid = (s + e)//2
#         # l = getMin(s, mid)
#         # r = getMin(mid+1, e)
#         # return min(l, r)
#
#
# print(getMin(0, len(arr)-1))
#
# import time
# start = time.time()
# N = int(input())
#
# def placeQueen(queen_pos):
#     res = 0
#     n = len(queen_pos)
#     if n == N:
#         return 1
#     for i in range(N):
#         for j in range(n):
#             if i == queen_pos[j]: break
#             if n - j == i - queen_pos[j]: break
#             if n - j == queen_pos[j] - i: break
#         else:
#             res += placeQueen(queen_pos + [i])
#     return res
#
# print(placeQueen([]))
# print(time.time()-start)



# 중복 순열
print('중복 순열')
arr = 'ABC'
N = len(arr)
for i in range(N):          # 첫번째 위치
    for j in range(N):      # 두번째 위치
        for k in range(N):  # 세번째 위치
            print(arr[i], arr[j], arr[k])

# 순열
print('순열')
arr = 'ABC'
N = len(arr)
for i in range(N):          # 첫번째 위치
    for j in range(N):      # 두번째 위치
        if i == j: continue
        for k in range(N):  # 세번째 위치
            if k == i or k == j: continue
            print(arr[i], arr[j], arr[k])

# 조합
print('조합')
arr = 'ABC'
N = len(arr)
for i in range(N):          # 첫번째 위치
    for j in range(i+1, N):      # 두번째 위치
        print(arr[i], arr[j])


# for 문을 통한 순열 생성 1
print('재귀 호출 1')
arr = [1, 2, 3, 4]
N = len(arr)
for i in range(N):
    arr[0], arr[i] = arr[i], arr[0]
    print(arr)
    arr[0], arr[i] = arr[i], arr[0] # 초기화


# for 문을 통한 순열 생성 2
print('재귀 호출 2')
arr = [1, 2, 3, 4]
N = len(arr)
for i in range(N):
    arr[0], arr[i] = arr[i], arr[0]
    for j in range(1, N):
        arr[1], arr[j] = arr[j], arr[1]
        print(arr)
        arr[1], arr[j] = arr[j], arr[1] # 초기화
    arr[0], arr[i] = arr[i], arr[0]


# for 문을 통한 순열 생성 3
print('재귀 호출 3')
arr = [1, 2, 3, 4]
N = len(arr)
for i in range(N):
    arr[0], arr[i] = arr[i], arr[0]
    for j in range(1, N):
        arr[1], arr[j] = arr[j], arr[1]
        for k in range(2, N):
            arr[2], arr[k] = arr[k], arr[2]
            print(arr)
            arr[2], arr[k] = arr[k], arr[2]
        arr[1], arr[j] = arr[j], arr[1] # 초기화
    arr[0], arr[i] = arr[i], arr[0]


# 재귀 호출!!!
print('재귀 호출!!!')
arr = [1, 2, 3, 4]
N = len(arr)

def perm(k):
    if k == N:
        print(arr)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k+1)
            arr[k], arr[i] = arr[i], arr[k]
perm(0)


import time
start = time.time()
# 재귀로 조합 구현하기
print('재귀로 조합!!!')
def nCr1(n, r):
    if n == r or r == 0:
        return 1
    else:
        # 하나의 원소를 포함하는 경우 + 하나의 원소를 포함하지 않는 경우
        return nCr1(n-1, r-1) + nCr1(n-1, r)

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def nCr2(n, r):
    if n == r or r == 0:
        return 1
    else:
        return fact(n) // (fact(n-r) * fact(r))


print(nCr1(30, 15))
print(nCr2(30, 15))
print(time.time()-start)

