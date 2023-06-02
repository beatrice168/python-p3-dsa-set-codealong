class MySet:
#    set = MySet([1, 2, 3, 3])

    def __init__(self,enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self,value):
        return value in self.dictionary 
    
    def add(self,value):
        self.dictionary[value]=True
        return self
    
    def delete(self,value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        len(self.dictionary)
    