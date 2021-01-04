import sys; sys.stdin = open('txt/1931_회의실배정.txt', 'r')

times = list()
for i in range(int(input())):
    times.append(list(map(int, input().split())))

times = sorted(times, key=lambda x:x[0])
times = sorted(times, key=lambda x:x[1])

meeting_count = 0
start_time = 0
for time in times:
    if time[0] >= start_time:
        start_time = time[1]
        meeting_count += 1
print(meeting_count)