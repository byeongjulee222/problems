lands_list = [[[1, 2], [2, 3]], [[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]]]
P_list = [3, 5]
Q_list = [2, 3]

# P: 추가, Q: 삭제
def solution(lands, P, Q):
    Min = 0xfffff
    Max = 0
    for land_ in lands:
        for height_ in land_:
            if height_ >= Max: Max = height_
            if height_ <= Min: Min = height_

    # print(Min, Max)
    # 높이를 바꿔가면서 land의 높이와 비교
    ans = 0xfffff
    for height in range(Min, Max+1):
        answer = 0
        for land in lands:
            for h in land:
                # 높이가 낮을 때 추가
                if h < height:
                    answer += (height-h) * P
                # 높이가 높을 때 삭제
                elif h > height:
                    answer += (h-height) * Q
        ans = min(answer, ans)

    return ans



def solution2(land, P, Q):
    answer = 0
    # 2중 리스트 일자화
    linear_land = sum(land, [])
    print(linear_land)
    linear_land.sort()
    N_square = len(land) ** 2
    max_count = int((N_square * Q) / (Q + P))
    print('max_count', max_count)
    small = linear_land[:max_count]
    big = linear_land[max_count:]
    mid = linear_land[max_count]
    print('linear_land', linear_land)
    print('small', small)
    print('big', big)
    print('mid', mid)
    answer += ((mid * len(small) - sum(small))) * P
    answer += (sum(big) - (mid * len(big))) * Q
    return answer

for i in range(2):
    lands = lands_list[i]
    P = P_list[i]
    Q = Q_list[i]

    # print(solution(lands, P, Q))
    print(solution2(lands, P, Q))
