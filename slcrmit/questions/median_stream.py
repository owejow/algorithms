import bisect 
from heapq import heappush, heappop, heapify
from functools import wraps

__all__ = ['median_brute_force', 'median_bisect', 'median_heapq']

# Median is the middle value in an ordered integer list. If the size of the list is even, 
# there is no middle value. So the median is the mean of the two middle value.
#
# Examples: 
# [2,3,4] , the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Given a stream of numbers return the median of the stream 
# after each step
# 
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7]
#
# gives [1,2,1,0,1,2,3,3]

def median_stream_brute_force(ary):
    values = []
    medians = []
    for i in range(len(ary)):
        values.append(ary[i])
        values.sort()
        median = (values[len(values)//2] + values[~(len(values)//2)])/2
        medians.append(median)
    return medians


def coroutine(func):
    """Decorator: primes `func` by advancing to first `yield`"""
    @wraps(func)
    def primer(*args,**kwargs):
        gen = func(*args,**kwargs)
        next(gen)
        return gen
    return primer


def median_heaps(max_heap, min_heap):
    median = -max_heap[0]
    
    if len(min_heap) == len(max_heap):
        median += min_heap[0]
        median /= 2.
        
    return median

def transfer_heap_value(heap_a, heap_b):
    heappush(heap_b, -heappop(heap_a))


@coroutine    
def median_stream_heap():
    min_heap = []
    max_heap = []
    
    median = None
    num = yield median
    
    heappush(max_heap, -num)

    median = median_heaps(max_heap, min_heap)
    num = yield median
    
    heappush(max_heap, -num)
    transfer_heap_value(max_heap, min_heap)
    while True:
        median = median_heaps(max_heap, min_heap)
        num = yield median

        
        equal_length = (len(max_heap) == len(min_heap))
        
        if num < median:
            if not equal_length:
                transfer_heap_value(max_heap, min_heap)
            heappush(max_heap, -num)
            
        else:
            if equal_length:
                transfer_heap_value(min_heap, max_heap)
            heappush(min_heap, num)

def median_streaming(ary):
    median_coroutine = median_stream_heap()
    return [median_coroutine.send(elem) for elem in ary]