import ctypes

class DynamicArray():
    def __init__(self):
        self.count = 0
        self.capacity = 1
        self.Arr = self._make_array(self.capacity)

    def __len__(self):
        return self.count

    def __getitems__(self, index):
        if 0<index<=self.capacity:
            return IndexError('Index out of bounds')
        return self.Arr[index]

    def append(self, item):
        if self.capacity== self.count:
            self._resize(self.Arr)
        self.Arr[self.count] = item
        self.count+=1

    def _resize(self, arr):
        self.capacity *=2
        spare = self._make_array(self.capacity)
        for i in range(len(arr):
            spare[i]=arr[i]
        arr = spare)
    
    def _make_array(self, capacity):
        return (capacity* ctypes.py_object)()
#Code Test
m = DynamicArray()

m.append('1')
m.append('random')
print(len(m))
