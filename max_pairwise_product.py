# python3
import random


def max_pairwise_product(numbers):
    first_biggest_number = max(numbers)
    copy_numbers = numbers.copy()
    copy_numbers.remove(first_biggest_number)
    second_biggest_number = max(copy_numbers)
    max_product = second_biggest_number * first_biggest_number

    return max_product

# function for stress test only
def max_pairwise_product_slow(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])
    return max_product



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

    # stress_test
    # while True:
    #     input_n = random.randint(2, 100)
    #     input_numbers = []
    #     for i in range(input_n):
    #         number = random.randint(1, 1000000)
    #         input_numbers.append(number)
        
    #     print(f"My fast function -> [{max_pairwise_product(input_numbers)}] and my slow function -> [{max_pairwise_product_slow(input_numbers)}]")
    #     if max_pairwise_product(input_numbers) != max_pairwise_product_slow(input_numbers):
    #         break
