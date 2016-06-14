# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    return binary_search2(a, x, left, right-1)

def binary_search2(arr, key, imin, imax, zero_based=True):
    if imax < imin:
        return -1
    else:
        imid = int(imin + (imax - imin) / 2)
        if arr[imid] > key:
            return binary_search2(arr, key, imin, imid - 1, zero_based)
        elif arr[imid] < key:
            return binary_search2(arr, key, imid + 1, imax, zero_based)
        else:
            if zero_based:
                return imid
            else:
                return imid + 1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
