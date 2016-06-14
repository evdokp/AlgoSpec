# Uses python3
import sys


def optimal_sequence2(n, sequence):
    if n > 10:
        #sequence.insert(0,n)
        sequence.append(n)
        if n % 3 == 0:
            return optimal_sequence2(int(n / 3), sequence)
        elif n % 2 == 0:
            return optimal_sequence2(int(n / 2), sequence)
        else:
            return optimal_sequence2(n - 1, sequence)
    else:
        if n < 2:
            return [1]
        m = 1
        tmpseq = []
        while n != m:
            if m * 3 > n:
                if m * 2 > n:
                    m += 1
                else:
                    m *= 2
            else:
                m *= 3
            tmpseq.insert(0, m)
        sequence.extend(tmpseq)
        sequence.append(1)
    return reversed(sequence)

def optimal_sequence(n):
    seq = []
    return optimal_sequence2(n, seq)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
