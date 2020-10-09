A_list = [[5,1,3,7], [2,2,2,2]]
B_list = [[2,2,6,8], [1,1,1,1]]

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        if B[i] > A[i]:
            answer += 1
    return answer

for i in range(2):
    A = A_list[i]
    B = B_list[i]
    print(solution(A, B))