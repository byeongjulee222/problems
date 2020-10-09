depar_list = ["SEOUL", "ULSAN"]
hub_list = ["DAEGU", "SEOUL"]
dest_list = ["YEOSU", "BUSAN"]
roads_list = [[["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]],
              [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]]


def dfs(cities, node, visited, dic):
    for i in dic[node]:
        if visited[cities.index(node)]:
            dfs(i)

def solution(depar, hub, dest, roads):
    first, second = 0, 0
    dic = dict()
    for road in roads:
        if road[0] not in dic:
            dic[road[0]] = [road[1]]
        else:
            dic[road[0]].append(road[1])

    visited = [False for _ in range(len(dic))]

    print(dic)
    cities = list(dic.keys())
    # 시작지점에서 물류창고
    dfs(cities, depar, visited, dic)

    if visited[cities.index(hub)]:
        first += 1

    return first
    # 물류창고에서 도착지점

for i in range(2):
    depar = depar_list[i]
    hub = hub_list[i]
    dest = dest_list[i]
    roads = roads_list[i]

    print(solution(depar, hub, dest, roads))
