import random
import time

def insertion_sort(x):
    if len(x) == 1:
        return x
    i, j = 0, 1
    while j < len(x):
        if x[j] >= x[i]:
            j += 1
            i += 1
        else:
            temp = j
            while i > -1 and x[j] < x[i]:
                x[i], x[j] = x[j], x[i]
                i -= 1
                j -= 1
            i = temp
            j = temp + 1
    return x

if __name__ == '__main__':
    x = list(range(10000))
    random.shuffle(x)
    start_time = time.time() 
    x = insertion_sort(x)
    end_time = time.time() - start_time
    print('First 100 sorted', x[:100])
    print('Time taken is', end_time)
