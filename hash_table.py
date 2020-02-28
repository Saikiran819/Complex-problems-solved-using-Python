class hashTable:
    
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] *self.size
        
    def hashing(self, key): 
        return key%self.size
        
    def insert(self, key, value):
        hashkey = self.hashing(key)
        
        if self.keys[hashkey] == None:
           self.keys[hashkey] = key
           self.values[hashkey] = value
            
        else:
            if self.keys[hashkey] == key:
                #self.values[hashkey] = value
            #else:
                hashkey = self.rehash(hashkey)
                self.keys[hashkey] = key
                self.values[hashkey] = value
    def rehash(self, key):
        hashkey = key
        while self.keys[hashkey] != None and self.values[hashkey] != None:
            hashkey = (hashkey+3) % self.size
        return hashkey

    def getValue(self, key):
        return self.values[key%self.size]
    def delete(self, key):
        del(self.values[key])
        del(self.keys[key])
    
a = hashTable(12)
a.insert(5, 10)
a.insert(3, 40)
a.insert(3, 50)
a.insert(3, 60)
a.insert(4, 20)
a.insert(2, 30)
a.insert(7, 70)

print(a.keys)
print(a.values)

print(a.getValue(7))
print(a.getValue(3))
