from typing import List, Optional
from serialize_deserialize_binary_tree import HelperTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST by defination, it means its inorder.
        # Idea 1 , do an inorder , and put in sorted and take the 1st index return 
        # writing inorder recursively is simple
        # lets do it iteratively ( why iterative ,w e use heap thats why its faster)
        # Trying to do an inorder traversal.
        # stack = []
        # cur = root
        # while stack or cur:
        #     while cur: # while cur is not left keep moving left
        #         stack.append(cur)
        #         cur = cur.left

        #     #popping element to visit tight v
        #     cur = stack.pop()

        #     k -=1
        #     if k ==0:
        #         return cur.val
        #     cur = cur.right

        # DFS inorder traveersal 
        # Time complexity O(n)
        arr = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return arr[k - 1] # Because array starts from 0 index 
    
if __name__ == "__main__":
    input_array = [5,3,6,2,4,None,None ,1]
    input_array = [3,1,4,None ,2]
    k = 1
    res = Solution()
    help_lib = HelperTree()
    root = help_lib.build_tree_from_array(input_array)
    print(res.kthSmallest(root , k))