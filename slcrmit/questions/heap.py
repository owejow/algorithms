from heapq import heapify, heappush, heappop

class HeapLazyRemove():

    def __init__(self, min_heap=False):
        self._min_heap = min_heap
        self._heap = []
        if min_heap:
            self._multiplier = 1 
        else: 
            self._multiplier = -1
        self._valid_count = 0
        self._invalid_values = {}

    def load(self, values):
        sanitized_values =  [self._sanitize_value(value) for value in values]
        self._valid_count += len(sanitized_values)
        self._heap = self._heap + sanitized_values
        self.heapify()
        
    def heapify(self):
        heapify(self._heap)

    def invalidate(self, value):
        self._increment_invalid(value)

    def push(self, value):
        heappush(self._heap, self._sanitize_value(value))
        self._valid_count += 1
        self._pop_invalids()
    
    def pop(self):
        value = self._sanitize_value(heappop(self._heap))
        self._valid_count -= 1
        self._pop_invalids()
        return value
    
    def peak(self):
        value = None
        if len(self._heap) > 0:
            value = self._heap[0]
        return self._sanitize_value(value)

    def _increment_invalid(self, value):
        if not self._is_invalid(value):
            self._invalid_values[value] = 0
        self._invalid_values[value] += 1
    
    def _decrement_invalid(self, value):
        if self._is_invalid(value):
            self._invalid_values[self._santize_value(value)] -= 1
    
    def _pop_invalids(self):
        while self._is_invalid(self.peak()):
            self._decrement_invalid(self.pop())
    
    def _sanitize_value(self,value):
        if value is not None:
             value *= self._multiplier
        return value

    def _is_invalid(self, value):
        result = False
        if value in self._invalid_values.keys():
            result = True
        return result
