# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

max1 = -1
max2 = -2
max1ind = -1


for i in range(0, n):
    if a[i] > max1:
        max1 = a[i]
        max1ind = i


for i in range(0, n):
    if max2 < a[i]:
        if a[i] < max1:
            max2 = a[i]
        elif a[i] == max1 and i != max1ind:
            max2 = a[i]


result = max1 * max2

#for i in range(0, n):
#    for j in range(i+1, n):
#        if a[i]*a[j] > result:
#            result = a[i]*a[j]

print(result)
