#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    scores, backtrack = lcs_scores_multi(a, b, c)
    return scores[len(a)][len(b)][len(c)]


def lcs_scores_multi(s1, s2, s3):
    s = [[[0 for y in range(len(s3)+1)] for x in range(len(s2)+1)] for z in range(len(s1)+1)]
    backtrack = [[[0 for y in range(len(s3)+1)] for x in range(len(s2)+1)] for z in range(len(s1)+1)]
    backtrack_options = [
        '+++',
        '++-',
        '+-+',
        '-++',
        '+--',
        '-+-',
        '--+'
    ]
    indelpen = 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            for k in range(1, len(s3) + 1):
                weight = 0
                if s1[i-1] == s2[j-1] and s1[i-1] == s3[k-1] and s2[j-1] == s3[k-1]:
                    weight = 1
                vars = [s[i-1][j-1][k-1] + weight,
                        s[i-1][j-1][k] - indelpen,
                        s[i-1][j][k-1] - indelpen,
                        s[i][j-1][k-1] - indelpen,
                        s[i-1][j][k] - indelpen*2,
                        s[i][j-1][k] - indelpen*2,
                        s[i][j][k-1] - indelpen*2]
                s[i][j][k] = max(vars)
                selected_var_ind = vars.index(s[i][j][k])
                backtrack[i][j][k] = backtrack_options[selected_var_ind]
    return s, backtrack


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
