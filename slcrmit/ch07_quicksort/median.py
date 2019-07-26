import math
from random import randint

def nlogn_median(lst):
    median = None
    if len(lst) > 0:
        lst.sort()
        median = (lst[len(lst)//2] + lst[~(len(lst)//2)]) / 2.
    return median

# algorithm that partitions a list at a given pivot.
#   Modified version of this algorithm will be used 
#    

def partition(lst, left, right):
    if len(lst) == 0:
        return None

    pivot = lst[right]
    i = left - 1

    for j in range(right):
        if lst[j] < pivot:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[right] = lst[right], lst[i+1]
    return i+1

# Average-case O(n)
# In the worst-case, a partition-based
# selection algorithm can take O(n^2) time.
#
#  ● Continuously pick the largest or
#    smallest element on each iteration.


def partition_randomized(lst, left, right, pivot):
    if len(lst) == 0:
        return None

    lst[right], lst[pivot] = lst[pivot], lst[right]

    pivot = lst[right]
    i = left - 1

    for j in range(right):
        if lst[j] < pivot:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[right] = lst[right], lst[i+1]
    return i+1


def select(lst, left, right, k):
    if left == right:
        return lst[left]

    pivot_index = randint(left, right)
    pivot_index = partition_randomized(lst, left, right, pivot_index)

    if k == pivot_index + 1:
        return lst[pivot_index]

    elif k < pivot_index + 1:
        right = pivot_index - 1

    else:
        left = pivot_index + 1

    return select(lst, left, right, k)

def quick_select(ary, k):
    return select(ary, 0, len(ary)-1, k)
    