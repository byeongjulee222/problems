import sys; sys.stdin = open("BJ_1244_switch.txt", "r")

# 남학생 : 스위치 번호가 자기가 받은 수의 배수이면 상태 변경
# 여학생 : 양 옆의 스위치를 보고, 스위치 상태가 같다면 바꾼다.
# (대칭되는 위치의 스위치 상태가 같을 때까지)
# 남학생 1, 여학생 2

N = int(input())
arr = list(map(int, input().split()))
stu_num = int(input())
# print(arr)
# print(stu_num)
for i in range(1, stu_num+1):
    x, switch = map(int, input().split())
    if x == 1:
        for j in range(1, len(arr)+1):
            if j % i == 0:
                if arr[i] == 1:
                    arr[i] = 0
                else:
                    arr[i] = 1
    else:
        for k in range(1, len(arr)+1):
            for l in range(len(arr)//2):
                if k-l >= 0 and k+l < len(arr):
                    if arr[k-l] == 1 and arr[k+l] == 1:
                        arr[k-l] = arr[k+l] = 0
                    elif arr[k-l] == 0 and arr[k+l] == 0:
                        arr[k-l] = arr[k+l] = 0
            break

print(arr)