import sys; sys.stdin = open('txt/17136_색종이 붙이기.txt', 'r')
import time

now = time.time()

def dfs(depth):
    global answer, total_one

    # 이미 최소값보다 depth가 커지면 더이상 탐색 안하고 리턴
    if answer > 0 and answer <= depth:
        return

    # 남은 1이 없을 때 depth가 최소값보다 작다면(최초에 answer는 -1)
    if total_one == 0:
        if answer == -1 or answer > depth:
            answer = depth  # 값을 할당하고 리턴
        return

    # 시작점을 정해야함.
    for x in range(10):
        for y in range(10):
            if MAP[x][y]:
                break
        if MAP[x][y]:
            break

    if x == 9 and y == 9 and MAP[x][y] == 0: return

    # 해당 점에 1~5 사이즈를 대본다.
    for size in range(1, 5 + 1):
        if paper[size]:
            one_zero = []  # 1 에서 0으로 바뀐 좌표 저장해서 나중에 도로 바꿔준다.

            if isCoverable(x, y, size):  # 해당 사이즈로 덮을 수 있다면
                for next_y in range(x, x + size):
                    for next_x in range(y, y + size):
                        MAP[next_y][next_x] = 0  # 1에서 0 으로 바꾸고
                        one_zero.append((next_y, next_x))  # 좌표를 저장

                #### 이 부분이 이해가 잘 안됨 ####
                # 왜 색종이 넓이만큼 빼고 더하는지?
                total_one -= size ** 2
                paper[size] -= 1
                dfs(depth + 1)

                # 다시 탐색을 위해 값을 되돌림
                paper[size] += 1
                total_one += size ** 2

                # 바뀐 좌표들을 다시 0에서 1로 바꿔줌
                for y_x in one_zero:
                    MAP[y_x[0]][y_x[1]] = 1


# 색종이로 채울 수 있는지 검사
def isCoverable(x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if 0 <= i < 10 and 0 <= j < 10:
                if MAP[i][j] == 0:
                    return False
            else:
                return False
    return True

# for _ in range(int(input())):
MAP = [list(map(int, input().split())) for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]
answer = -1
total_one = sum(sum(m) for m in MAP)
dfs(0)
print(answer)

print(paper)
print(time.time()-now)