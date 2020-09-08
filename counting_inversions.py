from copy import deepcopy

def sort_and_count(arr: list):
    if len(arr) == 1:
        return 0, arr
    else:
        half = int(len(arr) / 2)
        invs_a, a = sort_and_count(arr[:half])
        invs_b, b = sort_and_count(arr[half:])
        invs_c, c = merge_list(a, b)

    return (invs_a + invs_b + invs_c), c

def merge_list(left,right):
    result = list()
    i,j = 0,0
    inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv_count += (len(left)-i)
    result += left[i:]
    result += right[j:]
    return inv_count, result



with open('task_IntegerArray.txt', 'r') as f:
    arr = []
    for line in f:
        arr.append(int(line))

res, arr = sort_and_count(arr)
print(res)
