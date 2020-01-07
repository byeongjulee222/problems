def hanoi(k, start, mid, end):
    if k == 1:
        print(start, end)
    else:
        hanoi(k-1, start, end, mid)
        print(start, end)
        hanoi(k-1, mid, start, end)

N = int(input())

print(2**N-1)
hanoi(N, 1, 2, 3)