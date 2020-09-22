import ctypes

class DynamicArray():
    def __init__(self):
        self.count = 0
        self.capacity = 1
        self.Arr = self._make_array(self.capacity)

    def __len__(self):
        return self.count

    def __getitems__(self, index):
        return self.A[index]

    def append(self, item):
        if self.capacity== self.count:
            self._resize(self.A)
        self.A[count] = item
        self.count+=1

    def _resize(self):
        self.capacity *=2
        spare = self._make_array(self.capacity)
        for i in self.count:
            spare[i]=self.A[i]
        self.A = spare
    
    def _make_array(self, capacity):
        return (capacity* ctypes.py_object)()
