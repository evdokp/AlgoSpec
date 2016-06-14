# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments_sorted = sorted(segments, key=lambda segment: segment.end)
    while len(segments_sorted) > 0:
        x = segments_sorted[0].end
        points.append(x)
        segments_sorted = [s for s in segments_sorted if s.start > x]
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
