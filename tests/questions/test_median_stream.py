import slcrmit.questions.median_stream as subject

class TestMedianStream(object):
    def test_median_stream(self):
        ary = [1,2,3,4,5]
        expected = [1,1.5,2,2.5,3]
        median = subject.median_stream_brute_force(ary)
        assert median == expected
    
    def test_median_stream_complex(self):
        ary = [1,3,-1,-3,5,3,6,7]
        expected = [1,2,1,0,1,2,3,3]
        median = subject.median_stream_brute_force(ary)
        assert median == expected
    
    def test_median_stream_one_element(self):
        ary = [3]
        expected = [3]
        median = subject.median_stream_brute_force(ary)
        assert median == expected
    
    def test_median_stream_empty(self):
        ary = []
        expected = []
        median = subject.median_stream_brute_force(ary)
        assert median == expected

    def test_median_streaming_heaps_empty(self):
        ary = []
        expected = []
        median = subject.median_streaming_heaps(ary)
        assert median == expected