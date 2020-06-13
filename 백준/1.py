def solution(total_sp, skills):
    dic = dict()
    answer = [0 for _ in range(len(skills)+2)]

    for a, b in skills:
        if a not in dic.keys():
            dic[a] = [b]
        else:
            dic[a].append(b)

    for k, v in dic.items():
        if not len(v):
            answer[k] = 1
        else:
            answer[k] = len(v)

    for i in range(1, len(answer)):
        if not answer[i]:
            answer[i] = 1

    print(dic)
    print(answer)

    for i in range(len(answer)-1, 0, -1):
        print(i)
        if answer[i] == 1:
            continue
        else:
            answer[i] = 0
            for v in dic.values():
                for a in v:
                    answer[i] += answer[a]

    print(answer)


    return answer


skills = [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]
total_sp = 121
print(solution(total_sp, skills))



# def solution(n):
#     b = bin(n)[2:]
#     answer = 0
#
#     for i in range(len(b)):
#         if int(b[i]) == 1:
#             answer += 3 ** (len(b) - i - 1)
#     return answer
#
#
# print(solution(11))