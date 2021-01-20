import sys;sys.stdin=open('txt/2630_색종이 만들기.txt', 'r')

def divPaper(x, y, N):
    global cnt_white, cnt_blue
    # blue 종이의 개수를 직접 세어서 정사각형을 이루면 개수 +1
    tmp_cnt = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j]:
                tmp_cnt += 1
    if not tmp_cnt:
        cnt_white += 1
    elif tmp_cnt == N**2:
        cnt_blue += 1
    else:
        divPaper(x, y, N//2)
        divPaper(x + N//2, y, N//2)
        divPaper(x, y + N//2, N//2)
        divPaper(x + N//2, y + N//2, N//2)
    return

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt_white, cnt_blue = 0, 0

divPaper(0, 0, N)
print(cnt_white)
print(cnt_blue)



''' 다른 방법 (https://claude-u.tistory.com/268)
#쿼드 트리 함수 정의
def quad_tree(x, y, n):
    global matrix, blue, white #주어진 배열과 색 카운트 끌어오기
    color = matrix[y][x] #첫 색깔과 나머지 색이 같아야함
    double_break = False #for문 탈출용 double_break
    
    for i in range(x, x+n):
        if double_break:
            break
            
        for j in range(y, y+n):
            if matrix[j][i] != color: #하나라도 틀릴시에 재귀문 생성
                quad_tree(x, y, n//2) #2사분면
                quad_tree(x + n//2, y, n//2) #1사분면
                quad_tree(x, y + n//2, n//2) #3사분면
                quad_tree(x + n//2, y + n//2, n//2) #4사분면
                double_break = True #탈출!
                break
    
    if not double_break:
        if matrix[y][x] == 1: #파란색이라면
            blue += 1
        else:
            white += 1 #흰색이라면

N = int(input())
matrix = []
blue = 0
white = 0

#matrix 받기
for _ in range(N):
    matrix.append(list(map(int, input().split())))

quad_tree(0,0,N)
print(white)
print(blue)
'''