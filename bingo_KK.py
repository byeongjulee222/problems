answer = [[0] * 5 for _ in range(5)]
bingo_count = 0
count = 0

for number in range(len(numbers)):
    count += 1
    for y in range(len(bingo_arr)):
        for x in range(len(bingo_arr[y])):
            if numbers[number] == bingo_arr[y][x]: # 사회자가 부른 위치
                answer[y][x] = 1

    if bingo_count >= 3:
        break

print(count)