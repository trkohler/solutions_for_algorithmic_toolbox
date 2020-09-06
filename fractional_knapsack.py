def packing(capacity: int, arr: list) -> int:
    efficiency_arr = []
    max_value = 0

    for tup in arr:
        efficiency = tup[0] / tup[1]
        efficiency_arr.append(efficiency)
    
    while capacity:
        if efficiency_arr:
            max_eff = max(efficiency_arr)
            # print(max_eff)
            indx = efficiency_arr.index(max_eff)
            # print(indx)

            if capacity >= arr[indx][1]:
                max_value += arr[indx][0]
                # print("current max val ->", max_value)
                capacity -= arr[indx][1]
                # print("remaining capacity ->", capacity)
            else:
                part_weight = capacity
                part_value = (arr[indx][0] * part_weight) / arr[indx][1] 
                max_value += part_value
                capacity-= part_weight

            efficiency_arr.pop(indx)
            # print("eff err->", efficiency_arr)
            arr.pop(indx)
            # print('arr->', arr)
        else:
            break
    
    return max_value


n_items, capacity = input().split(" ")

arr = []
for _ in range(int(n_items)):
    value, weight = input().split(" ")
    v_w = tuple((int(value), int(weight)))
    arr.append(v_w)

print(packing(int(capacity), arr))
