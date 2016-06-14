# Uses python3
import sys

def gcd(a, b):
    if b == 0:
        return a
    arem = a % b
    return gcd(b, arem)

def lcm(a, b):
    return a * b // gcd(a, b)




x, y = map(int, input().split())
print(lcm(x, y))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

