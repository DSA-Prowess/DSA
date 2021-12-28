#Creating one empty queue

class EmptyQueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def enque(self,item):
        self.items.append(item)
    def deque(self):#deque operation is costly ,since the firest element is deleted all other elements are than shifted left
        if self.isEmpty():
            raise EmptyQueueError("Queue is empty")
        self.items.pop(0)
    def display(self):
        print(self.items)
    def peek(self):
        if self.isEmpty():
            raise  EmptyQueueError("Queue is empty cant be peeked")
        return  self.items[0]

class optimizedQueue:
    def __init__(self):
        self.items = []
        self.front = 0
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)- self.front
    def enque(self, item):
        self.items.append(item)
    def deque(self):
        if self.isEmpty():
            raise EmptyQueueError("Queue is empty")
        x = self.items[self.front]
        self.items[self.front] = None
        self.front = self.front + 1
        return x # returning the deleted element
    def peek(self):
        if self.isEmpty():
            raise EmptyQueueError("Queue is empty")
        return self.items[self.front]
    def display(self):
        print(self.items)


if __name__ == "__main__":
    # qu = Queue()
    # qu.enque(10)
    # qu.enque(20)
    # qu.enque(30)
    # qu.display()
    # print(qu.peek())
    # qu.deque()
    # qu.display()
    # print(qu.peek())
    # print(qu.size())
    qu = optimizedQueue()
    qu.enque(10)
    qu.enque(20)
    qu.enque(30)
    qu.display()
    print(qu.peek())
    qu.deque()
    qu.display()
    print(qu.peek())
    print(qu.size())