import sys; sys.stdin = open("txt/1966_arr_num.txt", "r")

def quick_sort(array):
    len_arr = len(array)
    if(len_arr <= 1):
        return array
    else:
        pivot = array[0]
        greater = [element for element in array[1:] if element > pivot]
        lesser = [element for element in array[1:] if element <= pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print('#{}'.format(tc), end=' ')
    print(*quick_sort(arr))