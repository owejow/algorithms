import slcrmit.ch07_quicksort.median as subject

class TestMedian(object):

    def test_median_nlogn(self):
        ary = [4,5,8,1,2,9]
        expected = 4.5
        median = subject.nlogn_median(ary)
        assert median == expected
    
    def test_median_nlogn_one_element(self):
        ary = [4]
        expected = 4
        median = subject.nlogn_median(ary)
        assert median == expected
    
    def test_median_nlogn_zero_elements(self):
        ary = []
        expected = None
        median = subject.nlogn_median(ary)
        assert median == expected
    
    def test_partition(self):
        ary = [0, 1, 6, 7, 4]
        expected = 2
        pivot_index = subject.partition(ary, 0, 4)
        assert pivot_index == expected
    
    def test_partition_single_element(self):
        ary = [0]
        expected = 0
        pivot_index = subject.partition(ary, 0, 0)
        assert pivot_index == expected
    
    def test_partition_empty(self):
        ary = []
        expected = 0
        pivot_index = subject.partition(ary, 0, 0)
        assert pivot_index == None

    def test_select_first(self):
        ary = [3,2,4]
        first_order = subject.select(ary, 0, 2, 1)
        assert first_order == 2
    
    def test_select_second_order(self):
        ary = [3,2,4]
        order_stat = subject.select(ary, 0, 2, 2)
        assert order_stat == 3
    
    def test_select_third_order(self):
        ary = [3,2,4]
        order_stat = subject.select(ary, 0, 2, 3)
        assert order_stat == 4
