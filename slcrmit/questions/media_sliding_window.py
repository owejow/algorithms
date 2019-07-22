import bisect 
from heapq import heappush, heappop, nsmallest 

__all__ = ['median_brute_force', 'median_bisect', 'median_heapq']

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


def median_heapq(nums, k):
    is_even = (k & 1) == 0
    medians = []
    
    window = sorted(nums[:k])
    min_queue = []
    max_queue = []

    for i in range(k//2):
        heappush(min_queue, window[i])

    for i in range(k//2, k):
        heappush(max_queue, -window[i])

    target_max = len(max_queue)
    target_min = len(min_queue)

    valid_max = target_max
    valid_min = target_min

    invalid_entries = {}

    for a, b in zip(nums, nums[k:] + [0]):
        medians.append(extract_median_heapq(
                                      min_queue, 
                                      max_queue, 
                                      is_even,
                                      k
                                      ) )
        insert_item_heapq(min_queue, 
                          max_queue, 
                          invalid_entries, 
                          valid_max, 
                          valid_min, 
                          is_even)

def extract_median_heapq(min_queue, 
                         max_queue, 
                         is_even,
                         k):
    if k == 1:
        median = min_queue[0]
    else:
        median = -max_queue[0]
        if is_even:
            median += min_queue[0]
            median /= 2.
    return median

def insert_item_heapq(min_queue, 
                      max_queue, 
                      invalid_entries, 
                      valid_max, 
                      valid_min, 
                      even):
    pass