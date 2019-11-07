import sys; sys.stdin = open('txt/4880.txt', 'r')

def tournament(i, j):
    # 부전승
    if i == j:
        return i

    # 가위 바위 보
    elif i + 1 == j:
        if (cards[i] == 1 and cards[j] == 2) or (cards[i] == 2 and cards[j] == 3) or (cards[i] == 3 and cards[j] == 1):
            return j
        else:
            return i

    # 왼쪽 그룹, 오른쪽 그룹 나누기
    # 그 그룹 안에서 재귀로 승부 진행
    else:
        a = tournament(i, (i+j)//2)
        b = tournament(((i+j)//2)+1, j)
        if (cards[a] == 1 and cards[b] == 2) or (cards[a] == 2 and cards[b] == 3) or (cards[a] == 3 and cards[b] == 1):
            return b
        else:
            return a


for tc in range(1, int(input())+1):
    N = int(input())
    cards = list(map(int, input().split()))
    print('#{} {}'.format(tc, tournament(0, N-1)+1))