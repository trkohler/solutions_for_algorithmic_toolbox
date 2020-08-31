# use the Pisano Period property. If you want to compute the last digit, Pisano Period of 10 will be 60. 

def fibonacci_sum(n):

    pisano = 60

    if n < 2: return n

    n %= pisano

    fib_arr = [1,1]
    for _ in range(n):
        fib_arr.append((fib_arr[-1] + fib_arr[-2]) % 10)

    return (fib_arr[-1] - 1) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
