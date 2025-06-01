
from typing import List, Optional
from serialize_deserialize_binary_tree import HelperTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right): # left and right are the lower(boundary) and upper(boundary).
            if not node:
                return True
            if not (node.val < right and node.val > left):  #not (A and B) is equivalent to (not A) or (not B). 
                return False
                    #Checking the left and right nboundary conditions           
            return (valid(node.left, left, node.val) and   # left subtree should be less , parent is set to right boundary , right boundary is updated 
                   valid(node.right, node.val, right)) # right subtree shoud  be more , left boundary is updated 
        return valid(root, float("-inf"), float("inf"))






if __name__ == "__main__":
    input_array = [5,1,4,None , None ,3,6]
    input_array = [2,1,3]
    res = Solution()
    help_lib = HelperTree()
    root = help_lib.build_tree_from_array(input_array)
    print(res.isValidBST(root))