A = list(range(1,13))

result = []
for subset in range(1 << len(A)):
    result.append([])

# print(result)

for i in range(1 << len(A)):
    for j in range(len(A)):
        if i & (1 << j):
            result[i].append(A[j])

print(result)