COMP_CNT = 0
def partiion(array, l_idx, r_idx):
    pivot = choose_pivot(array, arr_len)
    i = l_idx + 1
    j = l_idx + 1
    while j <= r_idx:
        if array[j] < pivot:
            swap = array[i]
            array[i] = array[j]
            array[j] = swap
            i += 1
    swap = array[i-1]
    array[i-1] = array[l_idx]
    array[l_idx] = swap        






def choose_pivot(array, arr_len):
    return array[0]


def quick_sort(array, arr_len):
    global COMP_CNT += arr_len - 1
    if arr_len == 1:
        return array, number_of_comparisons
    else:
        
        left = array[:pivot_idx]
        right = array[pivot_idx: array]
        quick_sort(left, len(left))
        quick_sort(right, len(right))

        return array, number_of_comparisons


with open ('quicksort.txt', 'r') as f:
    arr = []
    arr_len = 0
    d = f.read().split()
    for line in d:
        arr.append(int(line))
        arr_len+=1
    print(quick_sort(arr, arr_len)[1])