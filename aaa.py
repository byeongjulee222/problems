# def bfs_paths(graph, start, goal):
#     queue = [(start, [start])]
#     result = []
#
#     while queue:
#         n, path = queue.pop(0)
#         if n == goal:
#             result.append(path)
#         else:
#             for m in graph[n] - set(path):
#                 queue.append((m, path + [m]))
#     return result
#
# graph = {'A': set(['B', 'C']),
#          'B': set(['A', 'D', 'E']),
#          'C': set(['A', 'F']),
#          'D': set(['B']),
#          'E': set(['B', 'F']),
#          'F': set(['C', 'E'])}
#
# print(bfs_paths(graph, 'A', 'F'))

arr = [1, 2, 3, 4, 5]
n = len(arr)

for i in range(1<<n):
    print('{', end='')
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=',')
    print('}', end='\n')

a = '1 3 5'
print(type(a))