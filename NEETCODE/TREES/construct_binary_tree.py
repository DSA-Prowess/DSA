from typing import List ,Optional
from serialize_deserialize_binary_tree import HelperTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Recursive algorithm
        if not preorder or not inorder : # base case 
            return None 

        root = TreeNode(preorder[0]) # first value is root in preorder 
        mid = inorder.index(preorder[0]) # position of it in inorder (get the left and tight subtree)

        #Building the left subtree recursively
        # Checking left and right subarrays 
        root.left = self.build_tree(preorder[1:mid+1], inorder[:mid]) # ppropriating creating a sublist  ( left sublist )
        root.right = self.build_tree(preorder[mid+1:], inorder[mid+1:]) # after mid sublist  ( right sublist )
        return root 
    

if __name__ == "__main__":
  
    preorder = [-1]
    inorder = [-1]
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    help_lib = HelperTree()
    res = Solution()
    result = res.build_tree(preorder, inorder)
    print(result)
    print(help_lib.tree_to_array(result))