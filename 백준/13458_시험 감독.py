import sys; sys.stdin = open('txt/13458_시험 감독.txt', 'r')

# 각 방에 main은 무조건 한 명
for _ in range(int(input())):
    N = int(input())
    people = list(map(int, input().split()))
    main, sub = map(int, input().split())

    for person in people:
        person -= main
        # if person: 으로 했다가 계속 틀림 // 음수도 if문 결과로 True가 나옴
        if person > 0:
            if person%sub:
                N += person//sub + 1
            else:
                N += person // sub
    print(N)