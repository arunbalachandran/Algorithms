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
    if j - 1 >= 0 and x[i][j-1] >= x[i][j]:
        return peak_finder_greedy_2d(x, i, j-1)
    if i + 1 < len(x) and x[i+1][j] >= x[i][j]:
        return peak_finder_greedy_2d(x, i+1, j)
    if j + 1 < len(x[0]) and x[i][j+1] >= x[i][j]:
        return peak_finder_greedy_2d(x, i, j+1)
    if i - 1 >= 0 and x[i-1][j] >= x[i][j]:
        return peak_finder_greedy_2d(x, i, j)
    # if x[i][j] turns out to be the biggest among its neighbours
    return x[i][j] 

def peak_finder_wrapper(x):
    start = (0, 0)
    end = (len(x)-1, len(x[0])-1)
    return peak_finder_optimized(x, start, end)

# assumption that 'x' is always a 2d array
def peak_finder_optimized(x, start, end):
    global_mid_max = x[start[0]][start[1]]
    j = (start[1] + end[1]) // 2
    mid_max_indices = (start[0], start[1])
    for i in range(start[0], end[0]+1):
        if global_mid_max <= x[i][j]:
            global_mid_max = x[i][j]
            mid_max_indices = i, j 
    i, j = mid_max_indices
    if j - 1 >= start[1] and x[i][j-1] >= x[i][j]:
        return peak_finder_optimized(x, start, (end[0], j-1))      
    if j + 1 <= end[1] and x[i][j+1] >= x[i][j]:
        return peak_finder_optimized(x, (start[0], j+1), end)
    return x[i][j]
     

if __name__ == '__main__':
    # x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    x = np.random.randint(1000, size=(10000, 10000)) 
    start_time = time.time()
    greedy_answer = greedy_peak_wrapper(x)
    end_time = time.time() - start_time
    print('Greedy answer is', greedy_answer)
    print('Greedy wrapper took', end_time)
    start_time = time.time()
    optimized_answer = peak_finder_wrapper(x)
    end_time = time.time() - start_time
    print('Optimized answer is', optimized_answer)
    print('Optimized wrapper took', end_time)
