votes_list = [["AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "SOULFUL", "AVANT", "SANTA"],
              ["AAD", "AAA", "AAC", "AAB"]]
k_list = [2, 4]

from collections import Counter

def solution(votes, k):
    answer = ''
    Ct = Counter(votes)
    sorted_Ct = sorted(Ct.items(), key=lambda x: (-x[1], x[0]))
    Top_Sum = 0
    for i in range(k):
        Top_Sum += sorted_Ct[i][1]

    Bottom_Sum = 0
    j = 0
    while Top_Sum > Bottom_Sum:
        j -= 1
        Bottom_Sum += sorted_Ct[j][1]

    answer = sorted_Ct[j+1][0]

    return answer

for idx in range(2):
    votes = votes_list[idx]
    k = k_list[idx]
    print(solution(votes, k))