import sys; sys.stdin = open('txt/1486_장훈이의 높은 선반.txt', 'r')


# def janghoon(height, num):
#     global result
#     if height >= B:
#         result.append(height)
#     if num == N: return
#
#     janghoon(height+H[num], num+1)
#     janghoon(height, num+1)
#
#
# for tc in range(1, int(input())+1):
#     N, B = map(int, input().split())
#     H = list(map(int, input().split()))
#     # print(H)
#     result = []
#     janghoon(0, 0)
#     print(min(result)-B)




















# 모든 경우를 다 result에 넣고 최소값을 출력
# def find(height, num):
#     # 선반높이보다 높으면 result에 넣음
#     if height >= B:
#         result.append(height)
#     if num == N: return
#
#     # 높이 더하고 진행
#     find(height+arr[num], num+1)
#     # 높이 더하지않고 진행
#     find(height, num+1)
#
#
# for tc in range(1, int(input())+1):
#     N, B = map(int, input().split())
#     arr = list(map(int, input().split()))
#     result = []
#     find(0, 0)
#     print('#{} {}'.format(tc, min(result)-B))






def janghoon(n, height):
    global ans
    # print(height)
    if height > H:
        ans.append(height)

    if n == N: return

    janghoon(n+1, height)
    janghoon(n+1, height + arr[n])



# tc = int(input())
for tc in range(1, int(input())+1):
    N, H = map(int, input().split())
    # print(N, H)
    arr = list(map(int, input().split()))
    # print(arr)
    ans = []
    janghoon(0, 0)
    print("#{} {}".format(tc, min(ans)-H))























