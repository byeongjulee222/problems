n_list = [3, 2]
customers_list = [["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"],
                  ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]]

import datetime
def solution(n, customers):
    answer = 0
    arr = []
    for customer in customers:
        date, time, delay = customer.split()
        date_time = date + time
        date_time = datetime.datetime.strptime(date_time, '%m/%d%H:%M:%S')
        arr.append((date_time, int(delay)))

    kiosks_end = []
    dic = {}

    for i in range(n):
        kiosks_end.append(arr[i][0] + datetime.timedelta(minutes=arr[i][1]))
        dic[i] = 1


    for i in range(n, len(arr)):

        Min = min(kiosks_end)

        candi_kiosk = kiosks_end.index(Min)

        # 새로온 사람 도착 시간 < 키오스크 운영 완료 시간 --> 운영 완료 시간으로 대입

        # print(i)
        # print('비교', arr[i][0], Min)

        # Min: 키오스크들 중 끝나는 시간 가장 이른거
        if arr[i][0] < Min:
            # print('새로온 사람이 일찍옴')
            kiosks_end[candi_kiosk] = Min + datetime.timedelta(minutes=arr[i][1])
            # print(kiosks_end)
            dic[candi_kiosk] += 1
        # 새로온 사람 도착 시간 >= 키오스크 운영 완료 시간 --> 새로온 사람 도착 시간으로 대입
        else:
            # print('새로온 사람이 더 늦음')
            kiosks_end[candi_kiosk] = arr[i][0] + datetime.timedelta(minutes=arr[i][1])
            # print(kiosks_end)
            dic[candi_kiosk] += 1

    return max(dic.values())


for idx in range(2):
    n = n_list[idx]
    customers = customers_list[idx]

    print(solution(n, customers))