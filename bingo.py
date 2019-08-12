import sys
sys.stdin = open("bingo.txt", "r")

chulsoo_list = call_list = []
for _ in range(5):
    chulsoo_list += [input().split()]

for _ in range(5):
    call_list += input().split()

col_count_list = [0] * 5

result = []
how_many = 0
while bingo_count < 3:
# 값이 같을 때 'x'로 바꿔주기
    for call_num in call_list:
        how_many += 1
        for num_row in chulsoo_list:
            if call_num in num_row:
                num_row[num_row.index(call_num)] = 'x'
                # 행 단위로 빙고 찾기
                bingo_count = 0
                for i in chulsoo_list:
                    if i.count('x') == 5:
                        bingo_count += 1
                # 열 단위로 빙고 찾기
                for k in range(5):
                    for l in range(5):
                        if chulsoo_list[l][k] == 'x':
                            col_count_list[k] += 1
                            if col_count_list[k] == 5:
                                bingo_count += 1
                # 대각선 방향 빙고 찾기
                right_down_count = left_down_count = 0
                for m in range(5):
                    if chulsoo_list[m][m] == 'x':
                        right_down_count += 1
                        if right_down_count == 5:
                            bingo_count += 1                   
                    if chulsoo_list[4-m][m] == 'x':
                        left_down_count += 1
                        if left_down_count == 5:
                            bingo_count += 1
                if bingo_count == 3:
                    result.append(how_many)
                    break                            

print(how_many)