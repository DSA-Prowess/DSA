
# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        newHead = dummyHead = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next
            dummyHead = dummyHead.next
        
        # Attach the remaining part if any list is not exhausted
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
        
        return newHead.next

def print_linked_list(head: ListNode):
    """Helper function to print the linked list"""
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

if __name__ == "__main__":
    # Create two linked lists
    l1 = ListNode(1)    # 1 -> 2 -> 4
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    
    l2 = ListNode(1)    # 1 -> 3 -> 4
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    
    # Print the original lists
    print("Original List 1:")
    print_linked_list(l1)
    
    print("Original List 2:")
    print_linked_list(l2)
    
    # Merge the two linked lists
    sol = Solution()
    merged_head = sol.mergeTwoLists(l1, l2)
    
    # Print the merged linked list
    print("Merged linked list:")
    print_linked_list(merged_head)
