import sys
sys.stdin = open("repeat_word.txt", "r")

TC = int(input())

for repeat in range(TC):
    words = input()

    result = ''
    for idx, val in enumerate(words):
        result += val
        if val in result and words[idx+1:idx+1+len(result)] == result:
            break

    print('#{} {}'.format(repeat+1, len(result)))
