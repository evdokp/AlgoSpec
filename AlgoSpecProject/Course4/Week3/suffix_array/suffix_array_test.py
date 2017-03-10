import operator

from Course4.Week3.suffix_array.suffix_array_long import build_suffix_array

def counting_sort(array, maxval):
    """in-place counting sort"""
    n = len(array)
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return array


def sort_charecters(s):
    alphabet = {'$': 0, 'A': 1, 'C':2 , 'G':3, 'T':4 }
    order = [0 for _ in range(len(s))]
    count = [0 for _ in range(5)]
    for i in range(len(s)):
        count[alphabet[s[i]]] = count[alphabet [s[i]]] + 1
    for j in range(1, len(count)):
        count[j] = count[j] + count[j-1]
    for i in range(len(s) - 1,-1,-1):
        c = alphabet[s[i]]
        count[c] = count[c] - 1
        order[count[c]] = i
    return order

def compute_char_classes(s, order):
    cl = [0 for _ in range(len(s))]
    cl[order[0]] = 0
    for i in range(1, len(s)):
        if s[order[i]] != s[order[i-1]]:
            cl[order[i]] = cl[order[i - 1]] + 1
        else:
            cl[order[i]] = cl[order[i - 1]]
    return cl

def sort_doubled(s, l, order, cl):
    count = [0 for _ in range(len(s))]
    new_order = [0 for _ in range(len(s))]
    for i in range(len(s)):
        count[cl[i]] = count[cl[i]] + 1
    for j in range(1, len(s)):
        count[j] = count[j] + count[j-1]
    for i in range(len(s) - 1, -1, -1):
        start = (order[i] - l + len(s)) % len(s)
        cla = cl[start]
        count[cla] = count[cla] - 1
        new_order[count[cla]] = start
    return new_order

def update_classes(newOrder, cl, l):
    n = len(newOrder)
    newClass = [0 for _ in range(n)]
    newClass[newOrder[0]] = 0
    for i in range(1, n):
        cur = newOrder[i]
        prev = newOrder[i-1]
        mid = (cur + l) % n
        midPrev = (prev + l) % n
        if cl[cur] != cl[prev] or cl[mid] != cl[midPrev]:
            newClass[cur] = newClass[prev] + 1
        else:
            newClass[cur] = newClass[prev]
    return newClass


def build_suffix_array(s):
    order = sort_charecters(s)
    cl = compute_char_classes(s, order)
    l = 1
    while l < len(s):
        order = sort_doubled(s, l, order, cl)
        cl = update_classes(order, cl, l)
        l = 2 * l
    return order




#text = "AACGATAGCGGTAGA$"
#text = "GAGAGAGA$"
#ch = sort_charecters(text)
#print([text[i] for i in ch])

#sa = build_suffix_array(text)
#print(sa)
text = "AACGATAGCGGTAGA$"
order = sort_charecters(text)
cl = compute_char_classes(text, order)
neword = sort_doubled(text, 1, order, cl)
newcl = update_classes(neword, cl, 1)
print(newcl)


print(build_suffix_array('AACGATAGCGGTAGA$'))

#print(order)
#print(cl)
#print(neword)
#print(newcl)
#res = build_suffix_array(text)
#print(res)