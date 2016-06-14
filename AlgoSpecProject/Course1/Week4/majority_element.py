# Uses python3
import sys


def find_majority_element(a):
    candidate = a[0]
    vote = 1
    threshold = int(len(a) / 2)

    for x in a[1:]:
        if candidate == x:
            vote += 1
            continue
        if vote > 0:
            vote -= 1
            continue
        else:
            candidate = x
            vote = 1

    candidate_count = sum([1 for x in a if x == candidate])
    if candidate_count > threshold:
        return candidate
    else:
        return -1

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    candidate = a[0]
    vote = 1
    threshold = int(len(a) / 2)

    for x in a[1:]:
        if candidate == x:
            vote += 1
            continue
        if vote > 0:
            vote -= 1
            continue
        else:
            candidate = x
            vote = 1

    candidate_count = sum([1 for x in a if x == candidate])
    if candidate_count > threshold:
        return candidate
    else:
        return -1



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
