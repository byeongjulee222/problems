import sys; sys.stdin = open("txt/4831_electro_bus.txt", "r")

# T = int(input())
# for tc in range(1, T+1):

#     # K, N, M = 최대 이동거리, 종점 번호, 정류장 개수
#     K, N, M = map(int, input().split())
#     # 정류장 설치 리스트
#     arr = list(map(int, input().split()))
#     # print(arr)

#     location = cnt = 0
#     ride = True
#     while location < N-K and ride == True:
#         for i in range(K, 0, -1):
#             if location+i not in arr:
#                 ride = False
#             else:
#                 ride = True
#                 location += i
#                 cnt += 1
#                 break
#     if ride == False:
#         cnt = 0
        
#     print(cnt)


T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    location = cnt = 0
    ride = True
    while location < N - K and ride == True:
        for i in range(K, 0, -1):
            if location + i not in arr:
                ride = False
            else:
                location += i
                cnt += 1
                ride = True
                break
            
    if ride == False:
        cnt = 0
    print(cnt)

















