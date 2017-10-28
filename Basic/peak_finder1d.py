# naive version that just scans the list
import time

def peak_finder_naive(x):
    return max(x)

def peak_finder(x, start, end, mid):
    if mid == end or mid == start:
        return x[mid]
    if x[mid] < x[mid-1]:
        end = mid - 1
        return peak_finder(x, start, end, (start + end)//2)
    elif x[mid] < x[mid+1]:
        start = mid + 1
        return peak_finder(x, start, end, (start + end)//2)
    return x[mid]

if __name__ == '__main__':
    with open('primes.txt') as fp:
        text = fp.read()
        x = list(map(int, text.split()))

    start_time = time.time()
    # print (peak_finder_naive(x))
    print (peak_finder(x, 0, len(x)-1, len(x)//2))
    end_time = time.time() - start_time
    print ('Time taken :', end_time)
