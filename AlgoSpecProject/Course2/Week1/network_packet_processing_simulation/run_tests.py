from Course2.Week1.network_packet_processing_simulation.process_packages import Buffer, ProcessRequests, Request


def read_test_file(testnum):
    data = ''
    result = ''
    if testnum < 10:
        filename = '0' + str(testnum)
    else:
        filename = str(testnum)

    path = 'C:/GitHub/AlgoSpec/AlgoSpecProject/Course2/Week1/network_packet_processing_simulation/tests/' + filename
    with open(path) as f:
        input_lines = f.read().splitlines()

    first_line_data = [int(x) for x in input_lines[0].split()]
    buffer_size = first_line_data[0]
    requests_count = first_line_data[1]

    requests = []
    for request_line in input_lines[1:]:
        request_line_data = [int(x) for x in request_line.split()]
        arrival_time = request_line_data[0]
        process_time = request_line_data[1]
        request = Request(arrival_time, process_time)
        requests.append(request)

    responses = []
    path2 = path + '.a'
    with open(path2) as f:
        result = f.read().splitlines()
    for response_line in result:
        responses.append(int(response_line))


    return buffer_size, requests_count, requests, responses


for i in range(1, 23):
    buffer_size, requests_count, requests, expected_responses = read_test_file(i)
    buffer = Buffer(buffer_size)
    actual_responses_prep = ProcessRequests(requests, buffer)
    actual_responses = [response.start_time if not response.dropped else -1 for response in actual_responses_prep]
    passed = True
    for x in range(requests_count):
        if actual_responses[x] != expected_responses[x]:
            passed = False
            break

    if passed:
        print('test {0} passed'.format(i))
    else:
        print('test {0} failed'.format(i), 'expected', expected_responses, 'got', actual_responses)

