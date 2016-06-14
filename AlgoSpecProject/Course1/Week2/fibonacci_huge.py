# Uses python3
import sys

def get_pisano_period_len(m):
    fn1 = 0
    fn2 = 1
    pis_period = [fn1, fn2]
    d1 = fn1
    d2 = fn2
    isFirst = True
    isFinished = False;
    period_len = 0
    while not isFinished:
        period_len += 1
        fn = (fn1 + fn2) % m
        fn1, fn2 = fn2, fn
        d2, d1 = fn2, d2
        if isFirst:
            isFirst = False
        else:
            if d1 == 0 and d2 == 1:
                isFinished = True
        pis_period.append(fn)
    return period_len


def calc_fib(n):
    f1 = 0
    f2 = 1
    for i in range(2, n+1):
        fibnew = f1+f2
        f2, f1 = fibnew, f2
    return f2


def get_fibonaccihuge(n, m):
    return get_fib_huge_mod(n, m)

def get_fib_huge_mod(n, m):
    if n > 10:
        pp = get_pisano_period_len(m)
        rem = n % pp
        #print("rec case: rem({0}) = n({1}) / pp({2}), m={3}".format(rem, n, pp, m))
        if rem == 0:
            return 0
        if rem <= m or rem < n:
            return calc_fib(rem) % m
        return get_fib_huge_mod(rem, m)
    else:
        #print("base case", n, m)
        return calc_fib(n) % m


#res = get_fibonaccihuge(99999999999999999, 5)
#print(res)

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
