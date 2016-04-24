from Course2.Week1.check_brackets_in_code.check_brackets import balanced_brackets, balanced_brackets_1


def read_test_file(testnum):
    data = ''
    result = ''
    if testnum < 10:
        filename = '0' + str(testnum)
    else:
        filename = str(testnum)

    path = 'C:/GitHub/AlgoSpec/AlgoSpecProject/Course2/Week1/check_brackets_in_code/tests/' + filename
    with open(path) as f:
        data = f.read().splitlines()[0]

    path2 = path + '.a'
    with open(path2) as f:
        result = f.read().splitlines()[0]

    return data, result


for i in range(1,55):
    input_data, expected_result = read_test_file(i)
    actual_result = balanced_brackets_1(input_data)
    if actual_result == expected_result:
        print('test {0} passed'.format(i))
    else:
        print('expected {0}, got {1}, input: {2}'.format(expected_result, actual_result, input_data))