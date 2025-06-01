from typing import Optional, List
from serialize_deserialize_binary_tree import HelperTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Look at its children and swap the position 
        # Recursively run invertTree in left subtree and irght subtree
        if not root:
            return None
        
        #Swap the children 
        tmp = root.left
        root.left  = root.right
        root.right = tmp
        
        #DFS
        # preorder or postorder doesnt matter
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        

if __name__ == "__main__":
    input_array = [4,2,7,1,3,6,9]
    input_array = [2,1,3]
    help_lib = HelperTree()
    root = help_lib.build_tree_from_array(input_array)
    res = Solution()
    result = res.invertTree(root)
    result_array = help_lib.tree_to_array(result)
    print(result_array)