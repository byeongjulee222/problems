import sys; sys.setrecursionlimit(10**8)
def hanoi(n, _from, _by, _to):
    if n == 1:
        print("{} {}".format(_from, _to))
        return

    else:
        hanoi(n-1, _from, _to, _by)
        hanoi(1, _from, _by, _to)
        hanoi(n-1, _by, _from, _to)


# res = []
N = int(input())
print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 2, 3)