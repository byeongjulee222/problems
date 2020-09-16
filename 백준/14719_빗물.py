import sys; sys.stdin = open('txt/14719_빗물.txt', 'r')
# #
# def left(a, b):
#     while b >= 0:
#         if not board[a][b]:
#             b -= 1
#             continue
#         elif board[a][b]:
#             return 1
#     return False
#
# def right(a, b):
#     while b < x:
#         if not board[a][b]:
#             b += 1
#             continue
#         elif board[a][b]:
#             return 1
#     return False
#
# for _ in range(int(input())):
#     y, x = map(int, input().split())
#     arr = list(map(int, input().split()))
#     board = [list(0 for _ in range(x)) for _ in range(y)]
#     for i in range(x):
#         for j in range(arr[i]):
#             board[j][i] = 1
#
#     cnt = 0
#     for i in range(y):
#         for j in range(x):
#             if not board[i][j]:
#                 score = left(i, j) + right(i, j)
#                 if score == 2:
#                     cnt += 1
#
#     print(cnt)
#
# 4
# a a
# ab ba
# ring gnir
# newt twan
#
# # for _ in range(int(input())):
# #     word_1, word_2 = input().split()
# #     word_1 = list(word_1)
# #     word_2 = list(word_2)
# #     # print(word_1)
# #     cnt = 0
# #     flag = True
# #     for i in word_1:
# #         if i not in word_2:
# #             print("Impossible")
# #             flag = False
# #             break
# #         else:
# #             cnt += 1
# #     if cnt == len(word_1) and flag:
# #         print("Possible")
# #     elif flag:
# #         print("Impossible")


def solution(new_id):
    answer = ''
    string = ['-', '_', '.']
    # print(list(new_id))
    if new_id == '': return 'aaa'
    new_id = new_id.lower()
    alpha_list = list(new_id)

    result = []
    # 2단계
    for word in alpha_list:
        if word.isdigit() or word.isalpha() or word in string:
            result.append(word)

    # print(result)
    # print('result', result)
    # 3단계
    result2 = []
    for i in range(len(result)):
        if result[i] != '.':
            result2.append(result[i])
        else:
            if i+1 < len(result):
                # print(i)
                # print(result)
                if result[i+1] != '.':
                    result2.append(result[i])
    # print('result2', result2)


    # 4단계
    if not result2: return 'aaa'
    if result2[0] == '.':
        result2.pop(0)

    if result2[-1] == '.':
        result2.pop(-1)

    # print('result2', result2)
    # 5단계
    if not result2:
        result2.append('a')

    # 6단계
    if len(result2) > 15:
        result2 = result2[:15]

    # 7단계
    if len(result2) < 3:
        while len(result2) == 2:
            result2.append(result2[-1])


    if not result2: return 'aaa'
    if result2[0] == '.':
        result2.pop(0)

    if result2[-1] == '.':
        result2.pop(-1)

    for i in result2:
        answer += i

    return answer

for i in range(5):
    print(solution(input()))