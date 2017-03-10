def prefix_function(p):
    s = [0 for _ in range(len(p))]
    s[0] = 0
    border = 0
    whilecounter = 0
    for i in range(1, len(p)):
        while border > 0 and p[i] != p[border]:
            whilecounter += 1
            border = s[border-1]
        if p[i] == p[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return whilecounter, s

#s = 'ACATACATACACA'

s


a = prefix_function(s)
print(a)