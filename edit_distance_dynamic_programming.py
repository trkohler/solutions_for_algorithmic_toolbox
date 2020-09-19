import numpy as np


def levenshtein_distance(s, t):

    # Initialize matrix of zeros
    rows = len(s) + 1
    # print(s, len(s))
    cols = len(t) + 1
    # print(t, len(t))
    distance = np.zeros((rows, cols), dtype=int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1, cols):
            distance[i][0] = i
            distance[0][k] = k

    # print(distance)

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
    for row in range(1, rows):
        for col in range(1, cols):
            if s[row - 1] == t[col - 1]:
                distance[row][col] = distance[row - 1][col - 1]
                # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                distance[row][col] = min(
                    distance[row - 1][col] + 1,  # Cost of deletions
                    distance[row][col - 1] + 1,  # Cost of insertions
                    distance[row - 1][col - 1] + 1,
                )  # Cost of substitutions

        # print(distance)
    return distance[rows - 1][cols - 1]


first_string = input()
second_string = input()
result = levenshtein_distance(first_string, second_string)
print(result)
