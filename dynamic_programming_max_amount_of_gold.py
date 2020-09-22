import numpy as np


def dynamic_programming_knapsack(W: int, items: list) -> int:
    cols = W + 1
    rows = len(items) + 1

    matrix = np.zeros((rows, cols), dtype=int)
    for row in range(1, rows):
        for col in range(1, cols):
            if items[row - 1] == col:
                matrix[row][col] = max(matrix[row - 1][col], items[row - 1])
            elif items[row - 1] < col:
                matrix[row][col] = max(
                    matrix[row - 1][col],
                    items[row - 1] + matrix[row - 1][col - items[row - 1]],
                )
                # print(matrix[row][col])
            else:
                matrix[row][col] = matrix[row - 1][col]
                # print(matrix[row][col])

    # print(matrix)

    return matrix[rows - 1][cols - 1]


w, n = [int(x) for x in input().split(" ")]
items = [int(x) for x in input().split(" ")]
val = dynamic_programming_knapsack(w, items)
print(val)
