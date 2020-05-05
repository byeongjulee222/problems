def number():
    for num in range(1, 10001):
        num_list.append(num//1000 + (num//100)%10 + (num//10)%10 + num % 10 + num)


num_list = []
number()
cnt = 0
for i in range(1, 10001):
    if i not in num_list:
        print(i)
        cnt += 1

print(cnt) # 983 개