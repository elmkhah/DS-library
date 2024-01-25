class _Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    
    def first(self):
        if self.size()>0:
            return self.items[0]
        else:
            return None
    
    def size(self):
        return len(self.items)
    
    def secend(self):
        return self.items[1]