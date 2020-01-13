# num이 1부터 쭉 돌면서
# 666을 포함하면 cnt를 하나씩 올리고
# cnt가 N이 되는 순간 num을 출력
N = int(input())

cnt, num = 0, 0
while True:
    if '666' in str(num): cnt += 1
    if cnt == N: break
    num += 1

print(num)