n_list = [10, 7, 100]
groups_list = [[[1, 5],[2, 7],[4, 8],[3, 6]],
               [[6, 7],[1, 4],[2, 4]],
               [[1, 50], [1, 100], [51, 100]]]

ans = []
def backtrack(n, light, cnt):
    global ans
    # print(height)
    if light > H:
        ans.append(cnt)

    # range(light[0], light[1]+1)

    if n == len(groups): return

    backtrack(n+1, light, cnt+1)
    backtrack(n+1, light + groups[n], cnt+1)



def solution(n, groups):

    backtrack(0, [], 0)
    answer = 0
    return answer


for idx in range(3):
    n = n_list[idx]
    groups = groups_list[idx]
    print(solution(n, groups))