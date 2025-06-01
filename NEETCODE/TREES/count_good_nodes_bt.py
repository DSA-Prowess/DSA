"""Return good nodes in a Binary tree"""
from serialize_deserialize_binary_tree import HelperTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class Solution:
        # root node always count as good node 
        def dfs(self, node, maxVal):
            # empty tree no good node 
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0 #condition to check if its  a good value so far
            maxVal = max(maxVal, node.val) # maxVal refers to the maximum value seen so far

            # count the number of good nodes , recursively in left and irght subtree
            res += self.dfs(node.left, maxVal)
            res += self.dfs(node.right, maxVal)
            return res

        def dfs_main(self, root):
            return self.dfs(root, root.val)
        



if __name__ == "__main__":
    input_array = [3,1,4,3, None, 1 , 5]
    input_array = [3,3,None,4,2]
    help_lib = HelperTree()
    root = help_lib.build_tree_from_array(input_array)
    res = Solution()
    result = res.dfs_main(root)
    print(result)

