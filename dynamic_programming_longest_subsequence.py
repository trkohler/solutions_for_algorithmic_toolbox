import numpy as np


def lcs(sec_1: list, sec_2: list) -> int:
    rows = len(sec_1) + 1
    cols = len(sec_2) + 1

    distance = np.zeros((rows, cols), dtype=int)

    for row in range(1, rows):
        for col in range(1, cols):
            if sec_1[row - 1] == sec_2[col - 1]:
                distance[row][col] = distance[row - 1][col - 1] + 1
            else:
                distance[row][col] = max(distance[row][col - 1], distance[row - 1][col])

    return distance[rows - 1][cols - 1]


n = int(input())
sec_1 = [int(x) for x in input().split(" ")]
m = int(input())
sec_2 = [int(x) for x in input().split(" ")]
print(lcs(sec_1, sec_2))
