import slcrmit.questions.media_sliding_window as subject

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