from serialize_deserialize_binary_tree import HelperTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# when there is a split between the two nodes , than it is the lowest common ancestors
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Time comlexity = O(logN) = Height of a tree
        # Space complexity O(1)
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right # going the right subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left # going the left subtree
            else:
                # place where the split occured , LCA
                return cur
            


if __name__ == "__main__":
    input_array = [6,2,8,0,4,7,9,None ,None,3,5]
    p = 2 
    q = 8 
    p = TreeNode(2)
    q = TreeNode(8)
    help_lib = HelperTree()
    root = help_lib.build_tree_from_array(input_array)
    res = Solution()
    result = res.lowestCommonAncestor(root, p , q)
    # result is in TreeNode structure so you have to print the value 
    print(result.val)