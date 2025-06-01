from collections import deque
from typing import List, Optional
from serialize_deserialize_binary_tree import HelperTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """We are using BFS"""
        q = deque()
        res = []
        q.append(root) # to be observe in Bin tree right side view root is under [] list brackets, giving errror like Tree Object is not iterable
        # subtle error because we are using append here which is different from right side BT , where we dont use  q = deque([root]) 
        while q:
            level = []
            qlen = len(q)
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    #res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

if __name__ == "__main__":
    input_array = [3,9,20,None,None,15,7]
#      3
#     /  \
#     9   20
#    / \  / \
#    N  N 15 7
#Output : [[3],[9,20],[N,N],[15,7]
#Output : [[3],[9,20],[15,7]
    help_lib = HelperTree()
    root = help_lib.build_tree_from_array(input_array)
    res = Solution()
    result = res.levelOrder(root)
    print(result)