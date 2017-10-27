# naive version that just scans the list
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

x = [1, 5, 3, 1, 6, 7]
print (peak_finder(x, 0, len(x)-1, len(x)//2))
