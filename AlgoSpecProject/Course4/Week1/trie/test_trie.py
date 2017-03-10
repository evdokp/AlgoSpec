from Course4.Week1.trie.trie import Trie

def read_test_file(testnum):
    filename = 'sample' + str(testnum)

    path = 'D:/GitExtensionsRepos/AlgoSpec/AlgoSpecProject/Course4/Week1/trie/sample_tests/' + filename
    with open(path) as f:
        words = f.read().splitlines()[1:]

    result_dict = {}
    path2 = path + '.a'
    with open(path2) as f:
        result_lines = f.read().splitlines()

    for line in result_lines:
        split1 = line.split('->')
        split2 = split1[1].split(':')
        key = split1[0]
        if int(key) not in result_dict.keys():
            result_dict[int(key)] = {}
        result_dict[int(key)][split2[1]] = int(split2[0])
    return words, result_dict


#data,expected = read_test_file(2)
#t = Trie(data)
#actual = t.produce_output_dict()


#print(expected)
#print(actual)


t = Trie(['ATAGA','ATC','GAT'])
print(t.produce_output_dict())