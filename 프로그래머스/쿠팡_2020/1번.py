def solution(N):
    score = 1
    for zin in range(2, 10):
        num = N
        Max = 1
        while num:
            if num % zin:
                Max *= (num % zin)
            num = num // zin

        if score <= Max:
            score = Max
            zinbub = zin

    return [zinbub, score]


print('ans', solution(10))