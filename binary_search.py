def binary_search(arr: list, el: int, max: int, min: int) -> int:
    if max < min:
        return -1

    mid = min + (max - min) // 2

    if arr[mid] == el: 
        return mid 
    elif arr[mid] > el: 
        return binary_search(arr, min=min, max=mid-1, el=el) 
    else: 
        return binary_search(arr, min=mid + 1, max=max, el=el) 



arr = [int(x) for x in input().split(" ")[1:]]
searchable_nums = [int(x) for x in input().split(" ")[1:]]

result_arr = [binary_search(arr, el, len(arr)-1, 0) for el in searchable_nums]
for el in result_arr:
    print(el, end=" ")
