#Creating one empty queue

class EmptyQueueError(Exception):
    pass

class Queue:
    def __init__(self, default_size = 10):
        self.items = [None]* default_size
        self.front = 0
        self.count = 0

    def isEmpty(self):
        return self.items == []

    def size(self):
        return self.count

    def enque(self,item):
        if self.count == len(self.items):
            self.resize( 2*len(self.items))# resize the size of th unerlying list
        i = (self.front + self.count) % len(self.items)
        self.items[i] = item
        self.count+=1


    def deque(self):
        if self.isEmpty():
            raise EmptyQueueError("Queue is empty")
        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1 )% len(self.items)
        self.count -=1
        return x

    def display(self):
        print(self.items)

    def peek(self):
        if self.isEmpty():
            raise  EmptyQueueError("Queue is empty cant be peeked")
        return  self.items[self.front]

    def resize(self, newsize):
        old_list = self.items
        self.items = [None]*newsize
        i = self.front
        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (i+1)%len(old_list)
        self.front = 0

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
    qu = Queue(6)
    qu.enque(10)
    qu.enque(20)
    qu.enque(30)
    qu.display()
    print(qu.peek())
    qu.deque()
    qu.display()
    print(qu.peek())
    print(qu.size())