class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Implementation for Doubly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with 'dummy' head and tail nodes which makes 
        # edge cases for insert & remove easier.
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

    def insertEnd(self, val):
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode

    # Remove first node after dummy head (assume it exists)
    def removeFront(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    # Remove last node before dummy tail (assume it exists)
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def print(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, end=" -> ")
            curr = curr.next
        print()


if __name__ == "__main__":
    # Example usage:
    dll = LinkedList()
    dll.insertFront(1)
    dll.insertFront(2)
    dll.insertEnd(3)
    dll.insertEnd(4)

    print("Doubly Linked List:")
    dll.print()

    dll.removeFront()
    print("After removing front:")
    dll.print()

    dll.removeEnd()
    print("After removing end:")
    dll.print()
    # Output:
    # Doubly Linked List:
    # 2  ->
    # 1  ->     
    # 3  ->
    # 4  ->
    # After removing front:
    # 1  ->
    # 3  ->
    # 4  ->
    # After removing end:
    # 1  ->
    # 3  ->
    # 4  ->
    # 4  ->
    # None
    # 3  ->
    # 1  ->
    # 2  ->
    # None
    # 2  ->

    