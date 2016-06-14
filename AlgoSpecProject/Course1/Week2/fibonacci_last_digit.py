# Uses python3
import sys

def last_digit(n):
    return int(str(n)[-1])

def get_fibonacci_last_digit(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(last_digit(fib[i-1]) + last_digit(fib[i-2]))
    return last_digit(fib[n])

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
