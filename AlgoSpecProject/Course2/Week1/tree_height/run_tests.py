from Course2.Week1.tree_height.tree_height import TreeHeight


def read_test_file(testnum):
    data = ''
    result = ''
    if testnum < 10:
        filename = '0' + str(testnum)
    else:
        filename = str(testnum)

    path = 'C:/GitHub/AlgoSpec/AlgoSpecProject/Course2/Week1/tree_height/tests/' + filename
    with open(path) as f:
        data = f.read().splitlines()

    nodes_count = int(data[0])
    vertices = [int(x) for x in data[1].split()]

    path2 = path + '.a'
    with open(path2) as f:
        result = f.read().splitlines()[0]

    return nodes_count, vertices, result



for i in range(1, 25):
    nodes_count, vertices, expected_result = read_test_file(i)

    tree = TreeHeight()
    tree.load(nodes_count, vertices)
    actual_result = tree.compute_height()
    if str(actual_result) == str(expected_result):
        print('test {0} passed'.format(i))
    else:
        print('expected {0}, got {1}'.format(expected_result, actual_result))