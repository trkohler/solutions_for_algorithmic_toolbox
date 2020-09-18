def coin_change(number: int, coins: list) -> int:
    empty_arr = []
    for _ in range(number + 1):
        empty_arr.append(number + 1)  # filling array with dumb results

    empty_arr[0] = 0  # we know that 0 can exchange only 0 coins
    # print(empty_arr)

    for n in range(1, len(empty_arr)):
        # print(empty_arr[n])
        # print(n)
        for coin in coins:
            if coin <= n:
                # print(f"{coin} less than {n}")
                indx = (
                    n - coin
                )  # we search for number we can check what was previosly calculated
                indx_val = empty_arr[
                    indx
                ]  # we check what's the value in this number we previously calculated
                # we compare new potential change and old change which already stored in the array as dumb value
                winner = min(indx_val + 1, empty_arr[n])
                # we set winner to the calculated value
                empty_arr[n] = winner
            else:
                # if coin larger than current number we can't change the number with this coin
                continue

    return empty_arr[number]


number = int(input())
print(coin_change(number, [1, 3, 4]))
