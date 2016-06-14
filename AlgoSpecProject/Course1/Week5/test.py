# from 1 to n approach

def calc_op_num(n, store):
    if n in store:
        return store[n]
    if n == 1:
        store[1] = 0
        return 0
    if n == 2:
        store[2] = 0
        return 1
    if n == 3:
        store[3] = 0
        return 1
    if n > 3:
        options = []
        if n % 3 == 0:
            options.append(calc_op_num(int(n/3),store))
        if n % 2 == 0:
            options.append(calc_op_num(int(n/2),store))
        options.append(calc_op_num(n-1,store))
        res = min(options) + 1
        store[n] = res
        return res


store = dict()
print(calc_op_num(9000, store))


