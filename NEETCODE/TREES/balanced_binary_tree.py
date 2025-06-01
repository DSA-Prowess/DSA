from typing import Optional
from serialize_deserialize_binary_tree import HelperTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # nested recursion function.
        # Recursively do a bottom up approach 
        def dfs(root):
            # Do a recursive dfs to find the height of the left subtree and ehight of the right subtree
            # Check if it is balanced for every subtree
            if not root: return [True,0] # (boolean, height)
            
            left, right= dfs(root.left), dfs(root.right)
            # making sure that the left and right sub trees are balanced, from the root sub tress too./
            balanced = left[0] and right[0] and abs(left[1]- right[1])<=1
            return [balanced, 1 + max(left[1],right[1])] # [ balanced(entire tree is balaned or not) is a boolean , (height of current tree) left and right subtree are integers]
        
        return dfs(root)[0]  # returning boolean 
        # def dfs(root):
        #     if not root:
        #         return [True, 0]

        #     left, right = dfs(root.left), dfs(root.right)
        #     balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        #     return [balanced, 1 + max(left[1], right[1])]

        # return dfs(root)[0]

if __name__ == "__main__":
    input_array = [3,9,20,None,None,15,7]
    input_array = [1,2,2,3,3,None,None,4,4]
    help_lib = HelperTree()
    root = help_lib.build_tree_from_array(input_array)
    res = Solution()
    result = res.isBalanced(root)
    print(result)