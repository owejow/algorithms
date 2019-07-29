import slcrmit.questions.median_sliding_window as subject

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
    
    def test_median_heapq(self):
        ary = [8,2,7,3,1,5]
        expected = [5,2.5,4]
        median = subject.median_heapq(ary, 4)
        assert median == expected
    
    def test_increment_invalid(self):
        invalid = {}
        subject.increment_invalid(10,invalid,False)
        assert list(invalid.keys()) == [10]
        assert invalid[10] == 1
    
    def test_increment_invalid_negates_number_with_negate_true(self):
        invalid = {}
        subject.increment_invalid(10,invalid,True)
        assert list(invalid.keys()) == [-10]
        assert invalid[-10] == 1
    
    def test_decrement_invalid_does_nothing_if_key_nonexistent(self):
        invalid = {}
        subject.decrement_invalid(10,invalid,False)
        assert list(invalid.keys()) == []
    
    def test_decrement_invalid_removes_key_when_count_is_zero(self):
        invalid = {10: 1}
        subject.decrement_invalid(10,invalid,False)
        assert list(invalid.keys()) == []

    def test_pop_invalid_elements(self):
        heap = [1,2,4,5,4,5,5]
        invalid = {1: 1, 2: 1, 4:1, 5:1}
        subject.pop_invalid_elements(heap, invalid, negate=False)
        assert heap == [4, 5, 5, 5]
    
    def test_add_valid_elements(self):
        heap = [1,2,4,5,4,5,5]
        invalid = {1: 1, 2: 1, 4:1, 5:1}
        subject.add_valid_element(heap, -3, invalid, negate=False)
        assert heap == [-3, 4, 5, 5, 5]
    
    def test_pop_invalid_elements_negate(self):
        heap = [-5, -5, -4, -2, -1]
        invalid = {2:1, 4:1, 5:2}
        subject.pop_invalid_elements(heap, invalid, negate=True)
        assert heap == [-1]

    def test_transfer_valid(self):
        heap_a = [-5, -2, -4, -1, -1, -1, -1, 0]
        heap_b = [6, 7, 8, 8, 10]

        invalid = {1:3, 2:1, 4:1, 0:1, 'valid_max':2, 'valid_min':5}
        
        expected_b = [5, 7, 6, 8, 10, 8]
        expected_a = [-1, 0]
        expected_invalid = {0:1, 'valid_max': 1, 'valid_min':6 }

        subject.transfer_valid(heap_a, heap_b, invalid, first_max=True)

        assert expected_invalid == invalid
        assert sorted(heap_a) == sorted(expected_a)
        assert sorted(heap_b) == sorted(expected_b)

