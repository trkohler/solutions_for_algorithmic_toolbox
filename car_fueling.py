def min_number_of_stations(x: list, n: int, l: int, d: int) -> int:
    """
    x это набор координат.
    n это количество станций.
    л - это максимальное расстояние которое может проехать машина.
    d - дистанция которую нужно проехать
    """
    num_refills = 0 # what we are searching for
    current_refill = 0 # coordinate
    x = [0, *x, d]
    indx_curr = x.index(current_refill)
    # print(x)

    while indx_curr <= n:
        # print("curr indx before while loop ->", indx_curr)
        indx_last = indx_curr
        # print("last refill index ->", indx_last)
        while (indx_curr <= n) and (x[indx_curr + 1] - x[indx_last] <= l):
            indx_curr += 1
            # print("curr indx ->", indx_curr)
        if indx_curr == indx_last:
            return -1
        if indx_curr <= n:
            num_refills += 1

    return num_refills


d = int(input())
l = int(input())
n = int(input())
coordinates_x = [int(x) for x in input().split(" ")]

# print(min_number_of_stations([200, 375, 550, 750], 4, 400, 950))
print(min_number_of_stations(coordinates_x, n, l, d))
