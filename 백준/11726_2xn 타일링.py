def nn(num):
    if num == 1: return 1
    if num == 2: return 2
    if arr[num]: return arr[num]
    else:
        arr[num] = nn(num-1) + nn(num-2)
        return arr[num]

N = int(input())
arr = [0] * (N+2)
nn(N)
print(arr[N])