from copy import copy

def change(value: int) -> int:
    number_of_coins = 0
    value = copy(value)
    while value:
        if value % 10 == 0:
            number_of_coins += 1
            value = value - 10
        elif value % 5 == 0:
            number_of_coins += 1
            value = value - 5
        else:
            number_of_coins += 1
            value -= 1
    
    return number_of_coins


value = int(input())
print(change(value))
