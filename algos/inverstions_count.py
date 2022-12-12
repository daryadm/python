def merge_and_count(sorted_a1, sorted_a2):
    sorted_merged = []
    left_len = len(sorted_a1)
    right_len = len(sorted_a2)
    cnt=0
    i, j = 0, 0

    while i < left_len or j < right_len:
        if i == left_len:
            sorted_merged.append(sorted_a2[j])
            j+=1
        elif j == right_len:
            sorted_merged.append(sorted_a1[i])
            i+=1
        else:
            if sorted_a1[i] < sorted_a2[j]:
                sorted_merged.append(sorted_a1[i])
                i+=1
            else:
                sorted_merged.append(sorted_a2[j])
                cnt += left_len - i
                j+=1
    return sorted_merged, cnt

# print(merge_and_count([1,2,3,8],[4,5,6,7]))

def count_inversions(array, array_len):
    cnt = 0
    sorted_arr = []
    if array_len == 1:
        sorted_arr = array
    else:
        half_len = array_len // 2
        left = array[:half_len]
        right = array[half_len:]
        sorted_left, left_cnt = count_inversions(left, half_len)
        sorted_right, right_cnt = count_inversions(right, array_len - half_len)
        sorted_arr, split_cnt = merge_and_count(sorted_left, sorted_right)
        cnt = left_cnt + right_cnt + split_cnt
    return [sorted_arr, cnt]

with open ('IntegerArray.txt', 'r') as f:
#with open ('integer_array1.txt', 'r') as f:
    arr = []
    arr_len = 0
    d = f.read().split()
    for line in d:
        arr.append(int(line))
        arr_len+=1
    print(count_inversions(arr, arr_len)[1])
    #2407905288