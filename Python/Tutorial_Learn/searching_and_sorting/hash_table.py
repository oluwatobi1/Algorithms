class HashTable:

    def __init__(self, size):
        self.size = size
        self.val = [None]*self.size
        self.key = [None]*self.size

    def put(self, key, val):
        hash_val = self.hash_function(key)

        if self.val[hash_val] is None:
            self.key[hash_val] = key
            self.val[hash_val] = val

        else:
            if self.val[hash_val] == key:
                self.val[hash_val] = val

            else:
                rehash = self.rehash(hash_val)

                while self.key[rehash] is not None and self.key[rehash] != key:
                    rehash = self.rehash(rehash)

                if self.val[rehash] is None:
                    self.key[rehash] = key
                    self.val[rehash] = val
                else:
                    self.val[rehash] = val

    def get(self, item):
        start_key = self.hash_function(item)
        data = None
        found = False
        stop = False
        position = start_key

        while data is None and not found and not stop:
            if self.key[position] == item:
                data = self.val[position]
                found = True
            else:
                position = self.rehash(position)
                if position == start_key:
                    stop = True
        return data

    def hash_function(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash+1) % self.size

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)


h = HashTable(6)

h[1]= "one"

print(h[1])

