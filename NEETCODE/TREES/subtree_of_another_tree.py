# Definition for a binary tree node.
from typing import List, Optional
from serialize_deserialize_binary_tree import HelperTree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # understand recursively 
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        #comes here if they are not the same

        #Checking for the subtree  
        return (self.isSubtree(root.left,subRoot) \
        or self.isSubtree(root.right,subRoot))
    
    def sameTree(self, root, subRoot):
        # both trees are empty
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left,subRoot.left) and self.sameTree(root.right,
                                                                           subRoot.right))
        return False
        

if __name__ == "__main__":
    tree_array = [3,4,5,1,2]
    subtree_array = [4,1,2] 
    # tree_array = [3,4,5,1,2,None,None,None,None,0]
    # subtree_array = [4,1,2] 
    res = Solution()
    help_lib = HelperTree()
    tree_root = help_lib.build_tree_from_array(tree_array)
    sub_root = help_lib.build_tree_from_array(subtree_array)
    result = res.isSubtree(tree_root, sub_root)
    print(result)

