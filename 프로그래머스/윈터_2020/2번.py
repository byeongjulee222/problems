P_list = ["PM 01:00:00", "PM 11:59:59", "AM 11:59:59"]
N_list = [10, 1, 3]

import datetime
def solution(p,n):
    # print(type(p))
    date_time = datetime.datetime.strptime(p[3:], '%H:%M:%S') + datetime.timedelta(seconds=n)
    if p[0] == "P":
        date_time += datetime.timedelta(hours=12)

    # print(date_time)

    answer = str(date_time)[-8:]
    return answer

for idx in range(3):
    P = P_list[idx]
    N = N_list[idx]
    print(solution(P, N))