import ctypes

class DynamicArray(object):
    def __init__(self):
        self.size = 0
        self.cap = 1
        self.arr = self._make_array(self.cap)
    def __len__(self):
        return self.size
    def append(self, item):
        if self.size>=self.cap:
            self.arr = self._increase(self.arr)
        self.arr[self.size] = item
        self.size+=1
    def _increase(self, arr):
        self.cap = 2*self.cap
        new_arr = self._make_array(self.cap)
        for i in range(len(self.arr)):
            new_arr[i]=self.arr[i]
        self.arr = new_arr
        return self.arr    

    def __getitem__(self, key):
        return self.arr[key]
    def _make_array(self, cap):
        return (cap* ctypes.py_object)()
#Code Test
m = DynamicArray()

m.append('1')
m.append('random')
m.append('1')
m.append('random')
m.append('1')
m.append('random')
m.append('1')
m.append('random')
print(len(m))
print(m[:])