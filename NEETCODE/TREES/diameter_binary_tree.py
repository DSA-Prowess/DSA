from typing import Optional
from serialize_deserialize_binary_tree import HelperTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # res = 0

        # # Returns height
        # def dfs(root):
        #     nonlocal res #non local , will do the same thing as self.res

        #     if not root: #Basse case
        #         return 0
        #     left = dfs(root.left) #hypothsesus
        #     right = dfs(root.right) #Hypothesis
        #     temp = max(left,right)+1 # for temp passing to above 
        #     #res = max(res, left + right)
        #     ans = max(temp, 1+left+right) # becoming the karta dharta
        #     res = max(res, ans)
        #     return temp #height for curr , to make the recursion continued

        # dfs(root)
        # return res-1 # we are passing noded , so decrement 1 for edges 
        # Another way of solving 
        self.res = 0

        # Returns the height ( not the diameter )
        def dfs(curr):
            if not curr:
                return 0 

            left = dfs(curr.left)
            right = dfs(curr.right)
            # Below your doing two thing, update the result and return height of the tree
            self.res = max(self.res, left + right)
            return 1 + max(left,right) # +1 gaves the heigt wrt curr

        dfs(root)

        return self.res
    
if __name__ == "__main__":
    input_array = [1,2]
    input_array = [1,2,3,4,5]
    help_lib = HelperTree()
    res = Solution()
    root = help_lib.build_tree_from_array(input_array)
    result = res.diameterOfBinaryTree(root)
    print(result)
    