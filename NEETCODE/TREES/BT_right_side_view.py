# Definition for a binary tree node.
from typing  import List, Optional 
from serialize_deserialize_binary_tree import HelperTree
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """This solution is mainly BFS"""
    """Also known as level order traversal """
    def right_side_view(self, root: Optional[TreeNode]) -> List[int]:     
        res = []
        q = deque([root]) # observing we are not using append here as in level order traversal we used append 
        while q : # you can pop elements from the queue
            rightSide = None 
            qLen = len(q) # current level , 1 leval at at time 
            #Once this loop ends than only right side variable is updated 
            for i in range(qLen):
                node = q.popleft()
                if node:
                    # right side of the child 
                    rightSide = node 
                    q.append(node.left)
                    q.append(node.right)
            # right side appended to the result.
            if rightSide:
                res.append(rightSide.val)
        return res 


if __name__ == "__main__":
    input_array = [1,2,3,None,5,None,4]
    help_lib = HelperTree()
    root = help_lib.build_tree_from_array(input_array)
    res = Solution()
    result = res.right_side_view(root)
    print(result)