import numpy as np


def bin_search(n, a):
    start = 0
    end = len(a)
    mid = int((start + end) / 2)
    o = 0

    found = False

    while not found and (mid >= start or mid <= end):
        found = a[mid] == n
        o += 1
        if (found):
            print(" Found in index: {} in the {} attempt".format(mid, o))
            break
        if a[mid] < n:
            start = mid
        else:
            end = mid
        mid = int((start + end) / 2)


def bin_search_recurse(n, a, start, end, attempt):
    mid = int((start + end) / 2)
    attempt += 1
    if a[mid] == n:
        print(" Found in index: {} in the {} attempt".format(mid, attempt))
        return
    elif a[mid] < n:
        bin_search_recurse(n, a, mid, end, attempt)
    else:
        bin_search_recurse(n, a, start, mid, attempt)


x = 10000000
arr = np.arange(x)
i = x - 1

bin_search(i, arr)
bin_search_recurse(i, arr, 0, len(arr), 0)
