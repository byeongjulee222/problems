score_list = [[24,22,20,10,5,3,2,1], [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]]
k_list = [3, 2]

# 점수차가 k
def solution(k, score):
    diff = []
    for i in range(1, len(score)):
        diff.append(score[i] - score[i-1])

    print(diff)

    dic = {}
    for d in diff:
        if d not in dic:
            dic[d] = 1
        else:
            dic[d] += 1
    print(dic)

    # k개보다 많은 부정 점수차이들의 인덱스를 저장
    # 그 인덱스 -1, 인덱스에 해당하는 값을 셋으로 저장
    keys = []
    for key, val in dic.items():
        if val >= k:
            keys.append(key)
    print(keys)

    idxs = []
    for di in range(len(diff)):
        if diff[di] in keys:
            idxs.append(di)

    print(idxs)

    Set = set()
    for i in idxs:
        Set.add(score[i])
        Set.add(score[i+1])

    print(len(Set))


    return len(score) - len(Set)


for idx in range(2):
    score = score_list[idx]
    k = k_list[idx]
    print(solution(k, score))