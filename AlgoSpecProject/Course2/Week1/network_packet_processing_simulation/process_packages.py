# python3
from queue import Queue


class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time


class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []
        self.requestsprocessed = 0

    def RemoveExecuted(self, request):
        # remove all procesed items
        finished = False
        while self.ExecutedInQueueLeft(request.arrival_time):
            self.Dequeue()

    def ExecutedInQueueLeft(self, timestamp):
        if self.IsEmpty():
            return False
        return self.finish_time_[0] <= timestamp

    def IsFull(self):
        return len(self.finish_time_) == self.size

    def IsEmpty(self):
        return len(self.finish_time_) == 0

    def Dequeue(self):
        self.finish_time_.pop(0)

    def DropRequest(self):
        return Response(True, -1)

    def StartImmediately(self, request):
        # start to process immediately
        self.finish_time_.append(request.arrival_time + request.process_time)
        return Response(False, request.arrival_time)

    def Enqueue(self, request):
        last_finish_time = self.finish_time_[-1]
        new_finish_time = last_finish_time + request.process_time
        self.finish_time_.append(new_finish_time)
        return Response(False,last_finish_time)

    def Process(self, request):
        self.requestsprocessed += 1

        self.RemoveExecuted(request)
        if self.IsFull():
            return self.DropRequest()
        else:
            if self.IsEmpty():
                return self.StartImmediately(request)
            else:
                return self.Enqueue(request)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
