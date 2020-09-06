def max_revenue(n: int, profit_arr: list, clicks_arr: list) -> int:
    max_revenue = 0

    profit_arr.sort()
    clicks_arr.sort()

    while n:
        max_product = profit_arr[n-1] * clicks_arr[n-1]
        max_revenue += max_product
        n -= 1

    return max_revenue

n = int(input()) # number of ads and slots for ads
profit_arr = [int(x) for x in input().split(" ")]
clicks_arr = [int(x) for x in input().split(" ")]

print(max_revenue(n, profit_arr, clicks_arr))
