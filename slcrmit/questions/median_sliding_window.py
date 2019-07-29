import bisect 

from heapq import heappush, heappop, nsmallest 
from functools import wraps

__all__ = ['median_brute_force', 
           'median_bisect', 
           'median_heapq', 
           'increment_invalid',
           'decrement_invalid']

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

def coroutine(func):
    """Decorator: primes `func` by advancing to first `yield`"""
    @wraps(func)
    def primer(*args,**kwargs):
        gen = func(*args,**kwargs)
        next(gen)
        return gen
    return primer

def extract_median_heaps(max_heap, min_heap, invalid):
    median = min_heap[0]
    if invalid['valid_max'] == invalid['valid_min']:
        median += -max_heap[0]
        median /= 2.0
    return median

def increment_invalid(num, invalid, negate):
    if negate:
        num *= -1

    if num not in invalid:
        invalid[num] = 0

    invalid[num] += 1

def decrement_invalid(num, invalid, negate):
    if is_invalid(num, invalid, negate):
        if negate:
            num *= -1
        invalid[num] -= 1

        if invalid[num] == 0:
            del[invalid[num]]

def pop_invalid_elements(heap, invalid, negate):
    if len(heap) > 0:
        while is_invalid(heap[0], invalid, negate):
            decrement_invalid(heappop(heap), invalid, negate)      


def transfer_valid(heap_a, heap_b, invalid, first_max):
    heappush(heap_b, -heappop(heap_a))
    if first_max:
        invalid['valid_max'] -= 1
        invalid['valid_min'] += 1
    else:
        invalid['valid_min'] -= 1
        invalid['valid_max'] += 1

    pop_invalid_elements(heap_a, invalid, first_max)
    pop_invalid_elements(heap_b, invalid, first_max)

def add_valid_element(heap, entry, invalid, negate):
    pop_invalid_elements(heap, invalid, negate)
    heappush(heap, entry)  
    if negate:
        invalid['valid_max'] += 1
    else:
        invalid['valid_min'] += 1
    pop_invalid_elements(heap, invalid, negate)

def is_invalid(value, invalid, negate):
    if negate:
        return -value in invalid.keys()
    else:
        return value in invalid.keys()        

def median_heapq(nums, k):
    is_even = (k & 1) == 0
    medians = []
    
    window = sorted(nums[:k])
    min_queue = []
    max_queue = []

    heappush(max_queue, [-a for a in window[0:k//2]])
    heappush(min_queue, window[k//2:])

    target_max = len(max_queue)
    target_min = len(min_queue)

    invalid_entries = {'valid_max': target_max, 'valid_min': target_min}

    for a, b in zip(nums, nums[k:] + [0]):
        median = extract_median_heaps(max_heap, min_heap, invalid)
        medians.append(median)

        increment_invalid(a, invalid_entries, median)

        if a < median:
            invalid_entries['valid_max'] -= 1
        else: 
            invalid_entries['valid_min'] -= 1

        equal_entries = (invalid_entries['valid_max'] == invalid_entries['valid_min']) 

        if b >= median:
            if not equal_entries:
                transfer_valid(min_heap, max_heap, invalid_entries, first_max=False)
            add_valid(min_heap, b, invalid_entries, negate=False) 
        else:
            if equal_entries:
                transfer_valid(max_heap, min_heap, invalid_entries, first_max=True)
            add_valid(max_heap, b, invalid_entries, negate=True)
