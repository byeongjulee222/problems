N = int(input())
last = 0
for i in range(N):
    # print('i: ', i)
    arr = i
    result = 0
    while i:
        b = i % 10
        result += b
        i //= 10
        # print(i)
    # print('result+i : ', result + a)
    if result + arr == N:
        last = arr
        break

print(last)

# print(198 % 10)
# print(198 // 10)
# print(1//10)