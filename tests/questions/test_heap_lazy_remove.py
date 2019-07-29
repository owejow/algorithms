import slcrmit.questions.heap as subject

class TestMedianSlidingWindow(object):

    def test_heap_lazy_remove_load_works(self):
        heap = subject.HeapLazyRemove(min_heap=True)
        values = [1,2,3,4]
        heap.load(values)
        assert heap.pop() == values[0]
        assert heap.pop() == values[1]
        assert heap.pop() == values[2]
        assert heap.pop() == values[3]
    
    def test_heap_lazy_remove_load_works_for_max_heap(self):
        heap = subject.HeapLazyRemove(min_heap=False)
        values = [1,2,3,4]
        heap.load(values)
        assert heap.pop() == values[3]
        assert heap.pop() == values[2]
        assert heap.pop() == values[1]
        assert heap.pop() == values[0]
    
    def test_heap_pop_invalids(self):
        heap = subject.HeapLazyRemove(min_heap=True)
        values = [1,2,3,4,5,6]
        heap.load(values)
        heap.invalidate(2)
        heap.invalidate(3)

        assert heap.pop() == values[0]
        assert heap.pop() == values[3]
        assert heap.pop() == values[4]
        assert heap.pop() == values[5]

#    def test_transfer_valid(self):
#        heap_a = [-5, -2, -4, -1, -1, -1, -1, 0]
#        heap_b = [6, 7, 8, 8, 10]
#
#        invalid = {1:3, 2:1, 4:1, 0:1, 'valid_max':2, 'valid_min':5}
#        
#        expected_b = [5, 7, 6, 8, 10, 8]
#        expected_a = [-1, 0]
#        expected_invalid = {0:1, 'valid_max': 1, 'valid_min':6 }
#
#        subject.transfer_valid(heap_a, heap_b, invalid, first_max=True)
#
#        assert expected_invalid == invalid
#        assert sorted(heap_a) == sorted(expected_a)
#        assert sorted(heap_b) == sorted(expected_b)

