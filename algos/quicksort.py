
def partiion(array, l_idx, r_idx, pivot):
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
    return array[0]


def quick_sort(array, arr_len):
    number_of_comparisons = 0
    if arr_len == 1:
        return array
    else:
        pivot = choose_pivot(array, arr_len)
        partitioned_array = partiion(array, 0, len(array) - 1, pivot)
        left = partitioned_array[: partitioned_array.index(pivot) + 1]
        right = partitioned_array[partitioned_array.index(pivot) + 1 :]
        sorted_l = quick_sort(left, len(left))
        sorted_r = quick_sort(right, len(right))
        array = sorted_l + sorted_r

        return array


with open ('quicksort1.txt', 'r') as f:
    arr = []
    arr_len = 0
    d = f.read().split()
    for line in d:
        arr.append(int(line))
        arr_len+=1
    print(quick_sort(arr, arr_len))
    