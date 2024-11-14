from collections import defaultdict
import heapq
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}: {end - start:.5f} seconds')
        return result
    return wrapper

@timer
def bottom_up_dynamic_programming(fpath):
    # parse file
    with open(fpath) as num_file:
        f = num_file.read()
        triangle = []
        for line in f.split('\n'):
            triangle.append(list(map(int, line.split())))
    while not triangle[-1]:
        triangle.pop()
    # dp
    no_rows = len(triangle)
    for i in range(no_rows - 2, -1 , -1):
        current_row = triangle[i]
        prev_row = triangle[i + 1]
        for j in range(len(current_row)):
            current_row[j] += max(
                prev_row[j],
                prev_row[j + 1]
            )
    return triangle[0][0]

@timer
def top_down_memoization(fpath):
    # parse file
    with open(fpath) as num_file:
        f = num_file.read()
        triangle = []
        for line in f.split('\n'):
            triangle.append(list(map(int, line.split())))
    while not triangle[-1]:
        triangle.pop()
    no_rows = len(triangle)
    max_path_sums = [[float('-inf')]*(i + 1) for i in range(no_rows)]
    def helper(row, col, path_sum_so_far):
        if row == no_rows:
            return
        if path_sum_so_far + triangle[row][col] > max_path_sums[row][col]:
            max_path_sums[row][col] = path_sum_so_far + triangle[row][col]
            helper(row + 1, col, max_path_sums[row][col])
            helper(row + 1, col + 1, max_path_sums[row][col])
    helper(0, 0, 0)
    return max(max_path_sums[-1])
    
@timer
def modified_dijkstras_algorithm(fpath):
    # parse file
    with open(fpath) as num_file:
        f = num_file.read()
        triangle = []
        for line in f.split('\n'):
            triangle.append(list(map(int, line.split())))
    while not triangle[-1]:
        triangle.pop()
    # create graph
    graph = defaultdict(dict)
    index = 0
    n = sum([len(row) for row in triangle])
    for row_no, row in enumerate(triangle):
        for digit in row:
            if index + row_no + 1 < n:
                graph[index][index + row_no + 1] = digit
            else:
                graph[index][n] = digit
            if index + row_no + 2 < n:
                graph[index][index + row_no + 2] = digit
            else:
                graph[index][n] = digit
            index += 1
    graph[n] = {}
    # dijkstras algorithm
    dist = [float('-inf')]*(n + 1)
    dist[0] = 0
    pq = [(0, 0)]
    while pq:
        prev, node = heapq.heappop(pq)
        for ngbr, edge in graph[node].items():
            if edge - prev > dist[ngbr]:
                dist[ngbr] = edge - prev
                heapq.heappush(pq, (prev - edge, ngbr))
    return dist[n]
    
if __name__ == "__main__":
    print(
        bottom_up_dynamic_programming('solutions/problem67.txt'),
        top_down_memoization('solutions/problem67.txt'),
        modified_dijkstras_algorithm('solutions/problem67.txt')
    )