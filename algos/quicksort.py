number_of_comparisons = 0

def partiion(array, l_idx, r_idx, pivot):
    swap_p = array[l_idx]
    pivot_idx = array.index(pivot)
    array[l_idx] = pivot
    array[pivot_idx] = swap_p
    i = l_idx + 1
    j = l_idx + 1
    while j <= r_idx:
        if array[j] < pivot:
            swap = array[i]
            array[i] = array[j]
            array[j] = swap
            i += 1
        j += 1
    swap = array[i-1]
    array[i-1] = array[l_idx]
    array[l_idx] = swap

    return array


def choose_pivot(array, arr_len):
    pivot_l = array[0]
    pivot_r = array[-1]
    if arr_len % 2 == 0: 
        pivot_m = array[arr_len // 2 - 1]
    else:
        pivot_m = array[arr_len // 2]
    pivots = sorted([pivot_l, pivot_r, pivot_m])
    pivot = pivots[1]
    return pivot
    

def quick_sort(array, arr_len):
    global number_of_comparisons
    number_of_comparisons += arr_len - 1
    if arr_len == 1:
        return array, number_of_comparisons
    pivot = choose_pivot(array, arr_len)
    partitioned_array = partiion(array, 0, len(array) - 1, pivot)
    left = partitioned_array[: partitioned_array.index(pivot)]
    if left:
        sorted_l, number_of_comparisons = quick_sort(left, len(left))
    else:
        sorted_l = []
    right = partitioned_array[partitioned_array.index(pivot) + 1 :]
    if right:
        sorted_r, number_of_comparisons = quick_sort(right, len(right))
    else:
        sorted_r = []
    array = sorted_l + [pivot] + sorted_r

    return array, number_of_comparisons


with open ('quicksort.txt', 'r') as f:
    arr = []
    arr_leng = 0
    d = f.read().split()
    for line in d:
        arr.append(int(line))
        arr_leng+=1
    print(quick_sort(arr, arr_leng)[1])
