def greedy_peak_wrapper(x):
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

if __name__ == '__main__':
    x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(greedy_peak_wrapper(x))
