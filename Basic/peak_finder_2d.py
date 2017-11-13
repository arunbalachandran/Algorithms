# TODO: make the recursive version faster than the brute force version
# TODO: check why this version of peak finder is slower

import numpy as np
import sys
sys.setrecursionlimit(10000)
import time

def greedy_peak_wrapper(x):
    # the greedy algorithm with a small optimization
    if len(x[0]) == 1:  # if the list is a vector
        return max(map(lambda i: i[0], x))
    mid_i = (0 + (len(x) - 1))// 2
    mid_j = (0 + (len(x[0]) - 1))// 2
    return peak_finder_greedy_2d(x, mid_i, mid_j)

def peak_finder_greedy_2d(x, i, j):
    # use python shortcuting to avoid second conditional statement
    # shouldn't use this without a dry run of  the conditions being checked
    while True:
        if j - 1 >= 0 and x[i][j-1] > x[i][j]:
            j -= 1
            continue
        elif i + 1 < len(x) and x[i+1][j] > x[i][j]:
            i += 1
            continue
        elif j + 1 < len(x[0]) and x[i][j+1] > x[i][j]:
            j += 1
            continue
        elif i - 1 >= 0 and x[i-1][j] > x[i][j]:
            i -= 1
            continue
        # if x[i][j] turns out to be the biggest among its neighbours
        else:
            return x[i][j]

def peak_finder_wrapper(x):
    start = (0, 0)
    end = (len(x)-1, len(x[0])-1)
    return peak_finder_optimized(x, start, end)

# assumption that 'x' is always a 2d array
def peak_finder_optimized(x, start, end):
    j = (start[1] + end[1]) // 2
    global_mid_max = x[start[0]][j]
    mid_max_indices = (start[0], j)
    for i in range(start[0], end[0]+1):
        if global_mid_max < x[i][j]:
            global_mid_max = x[i][j]
            mid_max_indices = i, j
    i, j = mid_max_indices
    if j - 1 >= start[1] and x[i][j-1] >= x[i][j]:
        return peak_finder_optimized(x, start, (end[0], j-1))
    if j + 1 <= end[1] and x[i][j+1] >= x[i][j]:
        return peak_finder_optimized(x, (start[0], j+1), end)
    return x[i][j]


if __name__ == '__main__':
    # x = np.random.randint(100000, size=(10000, 10000))
    x = np.arange(100000000).reshape((10000, 10000))
    start_time = time.process_time()
    optimized_answer = peak_finder_wrapper(x)
    end_time = time.process_time() - start_time
    print('Optimized answer is', optimized_answer)
    print('Optimized wrapper took', end_time)
    start_time = time.process_time()
    greedy_answer = greedy_peak_wrapper(x)
    end_time = time.process_time() - start_time
    print('Greedy answer is', greedy_answer)
    print('Greedy wrapper took', end_time)
