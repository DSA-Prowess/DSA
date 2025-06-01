#Definition for a binary tree node.
# TIme complexity for Serialization and De- Serialization is O(n) , its basically trvaersals 
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class HelperTree():
     # Creating helper function to build tree
    def build_tree_from_array(self, arr):
        if not arr or arr[0] is None :
            return None 
        
        root = TreeNode(arr[0])
        queue = [root]
        i = 1
        while queue and i < len(arr):
            node = queue.pop(0)

            # left child 
            if i < len(arr) and arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i +=1 

            # Right child 
            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i +=1 

        return root 


    def tree_to_array(self, root):
        "Covert tree back to level order tree format "
        if not root:
            return []
        
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Reemvoe trailing None values 
        while result and result[-1] is None:
            result.pop()
        
        return result 

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        DFS using preorder traversal 
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return 

            # Preorder traversal 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        #print(",".join(res))
        return ",".join(res)
    
    
    def deserialize(self, data):
        """Decodes your encoded data(string delimitted by comma (,) ) to tree.
        The moment we reach two N's while reading , we pop back up to child node 
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0
        def dfs():
            # Bsae case when you reach two N values 
            if vals[self.i] == "N":
                self.i +=1  # moving on to next value 
                return None

            # Your are sort of reconstructing the Tree here in binary tree format  
            node = TreeNode(int(vals[self.i])) # root of node 
            self.i += 1
            node.left = dfs() # sekf.i incrementation is happening recursively 
            node.right = dfs()
            return node 
        return dfs()

# Your Codec object will be instantiated and called as such:
    # input= [1,2,3,None ,None ,4,5]
    # root = TreeNode(input[0])
    # root.left = TreeNode(input[1])
    # root.right = TreeNode(input[2])
    # root.left.left = None  # Dont create or pass using the TreeNode 
    # root.left.right = None 
    # root.right.left = TreeNode(input[5])
    # root.right.right = TreeNode(input[6])


    # ser = Codec()
    # print(ser.serialize(root))
    # deser = Codec()
    # print("After Deserialization ....................")
    # ans = deser.deserialize(ser.serialize(root))
    # print(ans)

#Test the code
if __name__ == "__main__":
    input_array = [1, 2, 3, None, None, 4, 5]

    # Build tree using helper function (recommended)
    codec = Codec()
    helper = HelperTree()
    root = helper.build_tree_from_array(input_array)

    print("Original array:", input_array)
    print("Serialized:", codec.serialize(root)) # Sending tree for serialization (cconverted into string s)

    # Deserialize and convert back to array
    deserialized_root = codec.deserialize(codec.serialize(root)) 
    result_array = helper.tree_to_array(deserialized_root)

    print("After deserialization:", result_array)
    print("Arrays match:", input_array == result_array)