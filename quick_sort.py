def quick_sort(arr, left_boundary, right_boundary):
    if left_boundary >= right_boundary:
        return

    index_pivot = partition(arr, left_boundary, right_boundary)
    quick_sort(arr, left_boundary, index_pivot-1)
    quick_sort(arr, index_pivot+1, right_boundary)

def partition(arr, left_boundary, right_boundary):
    pivot = arr[left_boundary]
    i = left_boundary + 1
    x = 0
    for j in range(left_boundary , right_boundary+1):
        x+=1
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[left_boundary], arr[i-1] = arr[i-1], arr[left_boundary]
    return i - 1, x


with open('quick_sort.txt', 'r') as file:
    arr = file.readlines()
    arr = [int(x) for x in arr]
    quick_sort(arr, 0, len(arr)-1)
