# Definition for a binary tree node.

from serialize_deserialize_binary_tree import HelperTree
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n) 
        # Space :O( h)  if its a balanced tree
        self.res = float("-inf")

        # return max path sum without split 
        def dfs(root):
            #nonlocal res
            if not root: #Base condition 
                return 0 
            leftMax = dfs(root.left) #hypothesis
            rightMax = dfs(root.right) #Hypothesis

            #Pattern code , same like diamter of a tree
            temp =max( root.val + max(leftMax, rightMax), root.val) # current node no splitting, also checking if negative childs, than take only root.
            ans = max(temp, leftMax + rightMax + root.val) #path that splits at current node)
            self.res = max(self.res, ans)
            #earlier code 
            # leftMax= max(leftMax, 0 )
            # rightMax = max(rightMax, 0)
            # #Compute max path sum with split 
            # res[0] = max( res[0], root.val+ leftMax + rightMax)

            return temp
        dfs(root)

        return self.res
    
if __name__ == "__main__":
    #Input: root = [1,2,3]
    #Output: 6
    #Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6
    # Input: root = [-10,9,20,null,null,15,7]
    # Output: 42
    # Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
    input_array =  [-10,9,20,None ,None ,15,7]
    input_array = [1, 2 ,3 ]
    max_path_sum = Solution()
    help_lib = HelperTree()
    root = help_lib.build_tree_from_array(input_array)
    result = max_path_sum.maxPathSum(root)
    print(result)