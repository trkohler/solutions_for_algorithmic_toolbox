# big thanks to Phat Le, author of (https://towardsdatascience.com/course-1-algorithmic-toolbox-part-4-dynamic-programming-223ffc01984a)
import sys


def evalt(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        raise Exception("Unsupported operand type!")


def get_maximum_value(dataset):
    for i in range(len(digits)):
        dp_max[i][i] = digits[i]
        dp_min[i][i] = digits[i]

    for s in range(0, len(digits)):
        for i in range(0, len(digits) - s - 1):
            j = i + s + 1
            min_value, max_value = min_max_value(i, j)
            dp_max[i][j] = max_value
            dp_min[i][j] = min_value


def min_max_value(i, j):
    min_value = sys.maxsize  # minus infinity
    max_value = -sys.maxsize  # plus infinity
    for k in range(i, j):
        a = evalt(dp_max[i][k], dp_max[k + 1][j], ops[k])
        b = evalt(dp_max[i][k], dp_min[k + 1][j], ops[k])
        c = evalt(dp_min[i][k], dp_max[k + 1][j], ops[k])
        d = evalt(dp_min[i][k], dp_min[k + 1][j], ops[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


if __name__ == "__main__":
    data = input()
    digits = [int(x) for x in data[0::2]]
    ops = [x for x in data[1::2]]
    dp_min = [[0 for x in range(len(digits))] for y in range(len(digits))]
    dp_max = [[0 for x in range(len(digits))] for y in range(len(digits))]
    get_maximum_value(data)
    print(dp_max[0][len(digits) - 1])
