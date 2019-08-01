import bisect 

from heapq import heappush, heappop, nsmallest 
from functools import wraps

__all__ = ['median_brute_force', 
           'median_bisect']

# Median is the middle value in an ordered integer list. If the size of the list is even, 
# there is no middle value. So the median is the mean of the two middle value.
#
# Examples: 
# [2,3,4] , the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.
# 
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

def median_brute_force(ary, k):
    medians = []
    for i in range(len(ary)-k+1):
        window = ary[i:i+k]
        median = (window[k//2] + window[~(k//2)])/2
        medians.append(median)
    return medians

def median_bisect(nums, k):
    window = sorted(nums[:k])
    medians = []
    for a, b in zip(nums, nums[k:] + [0]):
        # ~x == -x -1
        medians.append((window[k//2] + window[~(k//2)]) / 2.)
        window.remove(a)
        bisect.insort_right(window, b)
    return medians


# Utilize lazy removal from heaps to 
# implement more optimal performance. The performance.
# in the worst case will be n log(n). In the best case
# it should be n log(k). in the worst case the invalid
# values will never be popped from the heap.

def peak(heap, min_heap=True):
    if len(heap) == 0:
        return False

    value = heap[0]
    if not min_heap:
        value = -heap[0]

    return value

def median_heaps(max_heap, min_heap, balance):
    if balance == 0:
        median = (peak(max_heap, False) + peak(min_heap, True))/2

    elif balance > 0:
        median = peak(min_heap, True)

    else:
        median = peak(max_heap, False)
        
    return median

def transfer_heap_value(heap_a, heap_b, invalid, first_min_heap):
    heappush(heap_b, -heappop(heap_a))

    pop_invalid(heap_a, invalid, first_min_heap)

def is_invalid(value, valid):
    result = False
    if value in valid:
        result = True
    return result
        
def pop_invalid(heap, invalid, min_heap):
    while is_invalid(peak(heap, min_heap), invalid):
        popped_value = heappop(heap)
        if not min_heap:
            popped_value *= -1
        decrement_invalid(popped_value, invalid)

def increment_invalid(value, invalid):
    if value not in invalid:
        invalid[value] = 0
    invalid[value] += 1

def decrement_invalid(value, invalid):
    invalid[value] -= 1

    if invalid[value] == 0:
        del invalid[value]

def median_lazy_heap(nums, k):
    medians = []
    invalid = {}

    window = sorted(nums[:k])

    max_heap = [-elem for elem in window[:k//2]]
    min_heap = window[k//2:]

    balance = len(min_heap) - len(max_heap)

    for a, b in zip(nums, nums[k:] + [0]):
        median = median_heaps(max_heap, min_heap, balance)
        medians.append(median)

        increment_invalid(a, invalid)        

        if a < median or ((balance < 0) and (a == median)) :
            pop_invalid(max_heap, invalid, min_heap=False)
            balance += 1
        else:
            pop_invalid(min_heap, invalid, min_heap=True)
            balance -= 1

        if b < median:
            if balance < 0:
                transfer_heap_value(max_heap, min_heap, invalid, first_min_heap=False)
                balance += 2

            heappush(max_heap, -b)
            pop_invalid(max_heap, invalid, min_heap=False)
            balance -= 1
            
        else:
            if balance > 0:
                transfer_heap_value(min_heap, max_heap, invalid, first_min_heap=True)
                balance -= 2

            heappush(min_heap, b)
            pop_invalid(min_heap, invalid, min_heap=True)
            balance +=1

    return medians
