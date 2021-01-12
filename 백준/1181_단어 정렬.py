import sys; sys.stdin = open('txt/1181_단어 정렬.txt', 'r')

lst = set()
for num in range(int(input())):
    word = input()
    lst.add(word)

for w in sorted(lst, key=lambda x:(len(x), x)):
    print(w)