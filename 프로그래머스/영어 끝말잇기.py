n_list = [3, 5, 2]
words_list = [['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'],
              ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish',
               'hang', 'gather', 'refer', 'reference', 'estimate', 'executive'],
              ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']]

def solution(n, words):
    answer = []
    now = words[0]
    check = [now]
    for idx in range(1, len(words)):
        # 이미 사용한 단어이면 끝
        if words[idx] in check:
            return [idx % n + 1, idx // n + 1]
        # 끝말잇기 연결되면
        elif words[idx][0] == now[-1]:
            check.append(words[idx])
            now = words[idx]
            continue
        else:
            return [idx % n + 1, idx // n + 1]
    return [0, 0]


for i in range(3):
    n = n_list[i]
    words = words_list[i]
    print(solution(n, words))