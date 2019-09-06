import sys; sys.stdin = open("txt/1873_battle_field.txt", "r")

T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    move = int(input())
    work_list = list(input())
    # print(arr)
    # print(work_list)
    location = (0, 0, '')
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '<':
                location = (i, j, '<')
            elif arr[i][j] == '>':
                location = (i, j, '>')
            elif arr[i][j] == '^':
                location = (i, j, '^')
            elif arr[i][j] == 'v':
                location = (i, j, 'v')

    # print(start)
    for work in work_list:
        if work == 'S':
            if arr[location[0]][location[1]] == '<':
                if 0 <= location[1] < W:
                    for i in range(location[1]-1, -1, -1):
                        if arr[location[0]][i] == '#':
                            break
                        elif arr[location[0]][i] == '*':
                            arr[location[0]][i] = '.'
                            break
                        elif arr[location[0]][i] == '.' or arr[location[0]][i] == '-':
                            continue
            elif arr[location[0]][location[1]] == '>':
                if 0 <= location[1] < W:
                    for i in range(location[1]+1, W):
                        if arr[location[0]][i] == '#':
                            break
                        elif arr[location[0]][i] == '*':
                            arr[location[0]][i] = '.'
                            break
                        elif arr[location[0]][i] == '.' or arr[location[0]][i] == '-':
                            continue
            elif arr[location[0]][location[1]] == '^':
                if 0 <= location[0] < H:
                    for i in range(location[0]-1, -1, -1):
                        if arr[i][location[1]] == '#':
                            break
                        elif arr[i][location[1]] == '*':
                            arr[i][location[1]] = '.'
                            break
                        elif arr[i][location[1]] == '.' or arr[i][location[1]] == '-':
                            continue
            elif arr[location[0]][location[1]] == 'v':
                if 0 <= location[0] < H:
                    for i in range(location[0]+1, H):
                        if arr[i][location[1]] == '#':
                            break
                        elif arr[i][location[1]] == '*':
                            arr[i][location[1]] = '.'
                            break
                        elif arr[i][location[1]] == '.' or arr[i][location[1]] == '-':
                            continue

        elif work == 'U':
            if 0 <= location[0]-1 < H:
                if arr[location[0]-1][location[1]] == '.':
                    arr[location[0]][location[1]] = '.'
                    arr[location[0]-1][location[1]] = '^'
                    location = (location[0]+1, location[1], '^')
                elif arr[location[0]-1][location[1]] == '-':
                    for i in range(location[0]-1, -1, -1):
                        if arr[i][location[1]] == '#':
                            break
                        elif arr[i][location[1]] == '*':
                            arr[i][location[1]] = '.'
                            break
                        elif arr[i][location[1]] == '.' or arr[i][location[1]] == '-':
                            continue
                elif arr[location[0]-1][location[1]] == '*' or arr[location[0]-1][location[1]] == '#':
                    location = (location[0], location[1], '^')
        elif work == 'D':
            if 0 <= location[0]+1 < H:
                if arr[location[0]+1][location[1]] == '.':
                    arr[location[0]][location[1]] = '.'
                    arr[location[0]+1][location[1]] = 'v'
                    location = (location[0]-1, location[1], 'v')
                elif arr[location[0]+1][location[1]] == '-':
                    for i in range(location[0]+1, H):
                        if arr[i][location[1]] == '#':
                            break
                        elif arr[i][location[1]] == '*':
                            arr[i][location[1]] = '.'
                            break
                        elif arr[i][location[1]] == '.' or arr[i][location[1]] == '-':
                            continue
                elif arr[location[0]+1][location[1]] == '*' or arr[location[0]+1][location[1]] == '#':
                    location = (location[0], location[1], 'v')
        elif work == 'R':
            if 0 <= location[1]+1 < W:
                if arr[location[0]][location[1]+1] == '.':
                    arr[location[0]][location[1]] = '.'
                    arr[location[0]][location[1]+1] = '>'
                    location = (location[0], location[1]+1, '>')
                elif  arr[location[0]][location[1]+1] == '-':
                    for i in range(location[1]+1, W):
                        if arr[location[0]][i] == '#':
                            break
                        elif arr[location[0]][i] == '*':
                            arr[location[0]][i] = '.'
                            break
                        elif arr[location[0]][i] == '.' or arr[location[0]][i] == '-':
                            continue
                elif arr[location[0]][location[1]+1] == '*' or arr[location[0]][location[1]+1] == '#':
                    location = (location[0], location[1], '>')
        elif work == 'L':
            if 0 <= location[1]-1 < W:
                if arr[location[0]][location[1]-1] == '.':
                    arr[location[0]][location[1]] = '.'
                    arr[location[0]][location[1]-1] = '<'
                    location = (location[0], location[1]-1, '<')
                elif  arr[location[0]][location[1]-1] == '-':
                    for i in range(location[1]-1, -1, -1):
                        if arr[location[0]][i] == '#':
                            break
                        elif arr[location[0]][i] == '*':
                            arr[location[0]][i] = '.'
                            break
                        elif arr[location[0]][i] == '.' or arr[location[0]][i] == '-':
                            continue
                elif arr[location[0]][location[1]-1] == '*' or arr[location[0]][location[1]-1] == '#':
                    location = (location[0], location[1], '<')
    # print(arr)
    for i in arr:
        print(''.join(i))
