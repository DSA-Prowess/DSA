
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
        
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
        print(newHead.val)
        return newHead.next      


if __name__ == "__main__":
    # Create a new solution object
    sol = Solution()
    # Create a new linked list
    l1 = ListNode(1)    #1->2->4
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    # while l1:
    #     print(l1.val)
    #     l1 = l1.next
    # Create a new linked list
    l2 = ListNode(1)    # 1->3->4
    print(dir(l1))
    l2.next = ListNode(3)
    ListNode(3).next = ListNode(4)
    #l2.next.next = ListNode(4)
    # while l2:
    #     print(l2.val)
    #     l2 = l2.next
    # Merge the two linked lists
    newNode  = sol.mergeTwoLists(l1, l2)
    #print the merged linked list
    print("Merged linked list:")
    while newNode :
        print(newNode.val)
        newNode = newNode.next
    # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
    # Explanation: The merged linked list is 1 -> 1 -> 2 -> 3 -> 4 -> 4