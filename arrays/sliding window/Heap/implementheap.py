#Making the class constructor for heap 
# we always have to maintaing the structure and order property of the heap

class Heap:
    def __init__(self):
        #Empty heap that we have initialized. 
        self.heap = [0]


    def push(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1 # index of the last eleement that we have added
        #Percolate up (comparing with the root)
        while self.heap[i] < self.heap[i//2]:
            # below is the swapping happening move child to parent position 
            tmp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = tmp
            i = i//2
   
    #popping the element from the heap is more complemented that pushing the element in the heap.
    #if we remove a node , we should remove from the bottom of the tree, otherwise teh structure property of the heap will be violated
    # hence to maintain remove the last element and put it in the root and then percolate down
    def pop(self):
        #Swap the root with the last element
        self.heap[1] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        i = 1
        #Percolate down (comparing with the children)
        while i * 2 < len(self.heap):
            #Find the minimum child
            min_child = i * 2
            if i * 2 + 1 < len(self.heap) and self.heap[i * 2 + 1] < self.heap[i * 2]:
                min_child = i * 2 + 1
            #Swap
            if self.heap[i] > self.heap[min_child]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[min_child]
                self.heap[min_child] = tmp
                i = min_child
            else:
                break
    



#Time complexity : The height of the tree is O(logn)
#Time complexity : The tree is always balanced(complete binary tree), so the height of the tree is O(logn).
if __name__ == "__main__":
    heap = Heap()
    heap.push(3)
    heap.push(2)
    heap.push(1)
    print(heap.heap) # [0, 1, 3, 2]
    heap.pop()
    print(heap.heap) # [0, 2, 3]
    heap.pop()

    print(heap.heap) # [0, 3]