import sys; sys.stdin = open('txt/17136_색종이 붙이기.txt', 'r')
import time

now = time.time()

def dfs(depth):
    global Min, cnt_one

    # 이미 최소값보다 depth가 커지면 더이상 탐색 안하고 리턴
    if Min > 0 and Min <= depth:
        return

    # 남은 1이 없을 때 depth가 최소값보다 작다면(최초에 answer는 -1)
    if cnt_one == 0:
        if Min == -1 or Min > depth:
            Min = depth  # 값을 할당하고 리턴
        return

    # 1이 있는곳에서 시작(좌상단)
    for x in range(10):
        for y in range(10):
            if MAP[x][y]:
                break
        if MAP[x][y]:
            break

    # 끝까지 갔는데 그 자리가 0이면 조사할 필요없음
    if x == 9 and y == 9 and MAP[x][y] == 0: return

    # 해당 점에 1~5 사이즈를 대본다.
    for size in range(1, 5 + 1):
        # 종이가 남아있을 때 진행
        if paper[size]:
            one_zero = []  # 1 에서 0으로 바뀐 좌표 저장해서 나중에 도로 바꿔준다.

            if isCoverable(x, y, size):  # 해당 사이즈로 덮을 수 있다면
                # 색종이로 덮어지는 부분을 0으로 변경
                for next_x in range(x, x + size):
                    for next_y in range(y, y + size):
                        MAP[next_x][next_y] = 0  # 1에서 0 으로 바꾸고
                        one_zero.append((next_x, next_y))  # 좌표를 저장

                # 색종이가 붙여졌기 때문에 넓이만큼 1의 개수가 줄어듦
                cnt_one -= size ** 2
                paper[size] -= 1
                dfs(depth + 1)
                # 다시 탐색하기 위해 값을 되돌림
                paper[size] += 1
                cnt_one += size ** 2

            # 바뀐 좌표들을 다시 0에서 1로 바꿔줌
            for x_y in one_zero:
                MAP[x_y[0]][x_y[1]] = 1


# 색종이로 채울 수 있는지 검사
def isCoverable(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if i < 10 and j < 10:
                # 0인 곳에는 색종이가 붙으면 안된다. ****
                if MAP[i][j] == 0:
                    return False
            # 색종이가 MAP 범위를 벗어나면 안된다.
            else:
                return False
    return True

for _ in range(int(input())):
    MAP = [list(map(int, input().split())) for _ in range(10)]
    paper = [0, 5, 5, 5, 5, 5]
    Min = -1
    cnt_one = sum(sum(m) for m in MAP)
    dfs(0)
    print(Min)

    # print(time.time()-now)
