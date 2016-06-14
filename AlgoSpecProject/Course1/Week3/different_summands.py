# Uses python3
import sys


def get_summands(n, lowerlim):
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    if n == 2:
        return [2]

    result = []
    finished = False
    next_n = n
    while not finished:
        result.append(lowerlim)
        subprob_n = next_n - lowerlim
        lowerlim += 1

        # check for exit
        if subprob_n - lowerlim <= lowerlim:
            result.append(subprob_n)
            return result

        next_n = subprob_n

    return result


def get_summands2(n, lowerlim):
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    if n == 2:
        return [2]
    result = []
    result.append(lowerlim)

    subprob_n = n-lowerlim
    lowerlim += 1

    # check for exit
    if subprob_n - lowerlim <= lowerlim:
        result.append(subprob_n)
        return result
    result.extend(get_summands(subprob_n, lowerlim))

    return result

def optimal_summands(n):
    return get_summands(n,1)

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
