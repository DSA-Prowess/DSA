from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList( head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverses a singly linked list.

    Args:
        head (Optional[ListNode]): The head of the linked list to reverse.

    Returns:
        Optional[ListNode]: The new head of the reversed linked list.
    """
    prev = None
    curr = head

    while curr:
        next_node = curr.next  # Store the next node
        curr.next = prev       # Reverse the link
        prev = curr            # Move prev to current node
        curr = next_node       # Move to the next node

    return prev  # New head of the reversed linked list

if __name__ =="__main__":
    # Example usage:
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    #printing current link list
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


    # Reversing the linked list
    reversed_head = reverseLinkedList(head)

    # Printing the reversed linked list
    current = reversed_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
