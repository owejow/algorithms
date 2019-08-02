import slcrmit.questions.median_sliding_window as subject
from heapq import heapify

class TestMedianSlidingWindow(object):
    def test_median_sliding_window(self):
        ary = [1,2,3,4,5]
        expected = [2,3,4]
        median = subject.median_brute_force(ary, 3)
        assert median == expected

    def test_median_sliding_window_even(self):
        ary = [1,2,3,4,5,6]
        expected = [2.5,3.5,4.5]
        median = subject.median_brute_force(ary, 4)
        assert median == expected
    
    def test_median_sliding_empty(self):
        ary = []
        expected = []
        median = subject.median_brute_force(ary, 3)
        assert median == expected

    def test_median_bisect(self):
        ary = [5,8,2,1,2]
        expected = [5,2,2]
        median = subject.median_bisect(ary, 3)
        assert median == expected
    
    def test_median_bisect_even(self):
        ary = [8,2,7,3,1,5]
        expected = [5,2.5,4]
        median = subject.median_bisect(ary, 4)
        assert median == expected
    

    # lasy remove methods
    def test_peak(self):
        heap = [1,2,3,4]
        heapify(heap)
        assert  1 == subject.peak(heap, min_heap=True)
        assert -1 == subject.peak(heap, min_heap=False)

    def test_median_heaps(self):
        min_heap = [ 5, 6,  7, 8]
        max_heap = [-3, 2, -1, 4]
        heapify(min_heap)
        heapify(max_heap)
        assert 4 == subject.median_heaps(max_heap, min_heap, balance=0)
        assert 3 == subject.median_heaps(max_heap, min_heap, balance=-1)
        assert 5 == subject.median_heaps(max_heap, min_heap, balance=1)
    
    def test_increment_invalid(self):
        invalid = {1:3}
        subject.increment_invalid(1, invalid) 
        assert invalid == {1:4}
        subject.increment_invalid(5, invalid) 
        assert invalid == {1:4, 5:1}
    
    def test_decrement_invalid(self):
        invalid = {1:2}
        subject.decrement_invalid(1, invalid) 
        assert invalid == {1:1}
        subject.decrement_invalid(1, invalid) 
        assert invalid == {}
    
    def test_is_invalid(self):
        invalid = {1:2, 3:1}
        assert subject.is_invalid(1, invalid) 
        assert not subject.is_invalid(4, invalid) 

    def test_pop_invalid(self):
        heap = [1,2,3,4,5,6]
        invalid = {1:1, 2:1, 3:1, 4:1, 5:1}
        subject.pop_invalid(heap, invalid, min_heap=True)
        assert heap == [6]
        assert invalid == {}
    
    def test_pop_invalid_pops_nothing_if_top_valid(self):
        heap = [1,2,3,4,5,6]
        invalid = {2:1, 3:1, 4:1, 5:1}
        subject.pop_invalid(heap, invalid, min_heap=True)
        assert heap == [1,2,3,4,5,6]
        assert invalid == {2:1, 3:1, 4:1, 5:1}
    
    def test_pop_invalid_works_with_max_heap(self):
        heap = [-1,-2,-3,4,5,6]
        invalid = {1:1, 2:1, 3:1, 4:1, 5:1}
        subject.pop_invalid(heap, invalid, min_heap=False)
        assert heap == [4,5,6]
        assert invalid == {4:1, 5:1}

    def test_transfer_heap_value_min_heap_all_valid(self):

        invalid = {}
        min_heap = [6,7,8,9]
        max_heap = [-5,-4,-3]

        subject.transfer_heap_value(min_heap, max_heap, invalid, first_min_heap=True)
        assert invalid == {}
        assert sorted(min_heap) == sorted([7,8,9])
        assert sorted(max_heap) == sorted([-6,-5,-4,-3])
    
    def test_transfer_heap_value_max_heap_all_valid(self):

        invalid = {}
        min_heap = [6,7,8]
        max_heap = [-5,-4,-3,-2]

        subject.transfer_heap_value(max_heap, min_heap, invalid, first_min_heap=False)
        assert invalid == {}
        assert sorted(min_heap) == sorted([5,6,7,8])
        assert sorted(max_heap) == sorted([-4,-3,-2])
    
    def test_transfer_heap_value_max_heap_with_invalid(self):

        invalid = {4:1, 3:1, 7:1, 8:1}
        min_heap = [6,7,8]
        max_heap = [-5,-4,-3,-2]

        subject.transfer_heap_value(max_heap, min_heap, invalid, first_min_heap=False)
        assert invalid == {7:1, 8:1}
        assert sorted(min_heap) == sorted([5,6,7,8])
        assert sorted(max_heap) == sorted([-2])

    def test_transfer_heap_value_min_heap_with_invalid(self):

        invalid = {4:1, 3:1, 7:1, 8:1}
        min_heap = [6,7,8,9]
        max_heap = [-5,-4,-3,-2]

        subject.transfer_heap_value(min_heap, max_heap, invalid, first_min_heap=True)
        assert invalid == {3:1, 4:1}
        assert sorted(min_heap) == sorted([9])
        assert sorted(max_heap) == sorted([-6,-5,-4,-3,-2])

    def test_median_lazy_heap(self):
       input = [2, 5, 6, 3, 3, 9, 8, 4, 0, 2] 

       medians = subject.median_lazy_heap(input, 3)
       assert medians == [5, 5, 3, 3, 8, 8, 4, 2]
    
    def test_median_lazy_heap_window_1(self):
       input = [2, 5, 6, 3, 3, 9, 8, 4, 0, 2] 

       medians = subject.median_lazy_heap(input, 1)
       assert medians == [2, 5, 6, 3, 3, 9, 8, 4, 0, 2] 
    
    def test_median_lazy_heap_window_two(self):
       input = [2, 5, 6, 3, 3, 9, 8, 4, 0, 2] 

       medians = subject.median_lazy_heap(input, 2)
       assert medians == [3.5, 5.5, 4.5, 3, 6, 8.5, 6, 2, 1] 
       