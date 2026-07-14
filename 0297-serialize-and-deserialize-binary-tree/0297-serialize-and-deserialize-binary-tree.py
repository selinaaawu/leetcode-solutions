# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        ## INORDER BFS | time: O(n), space: O(n)
        # inorder saves level by level
        if not root:
            return "N"

        result = []
        queue = deque([root])
        while queue:
            # pop leftmost node
            node = queue.popleft()

            # if node missing -> store "N"
            if not node:
                result.append("N")
            # if node exists -> store node, append left/right
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        
        return ",".join(result)


        ## PREORDER DFS | time: O(n), space: O(n)
        # if value node -> store value
        # if null node -> store "N"

        # store preorder traversal in result list
        result = []

        def dfs(root):
            if not root:
                result.append("N")
                return
            
            result.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        # join result with comma, return as string
        return ",".join(result)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        ## INORDER BFS | time: O(n), space: O(n)
        result = data.split(",")

        if result[0] == "N":
            return None

        # create queue with root
        root = TreeNode(int(result[0]))
        queue = deque([root])

        index = 1
        while queue:
            node = queue.popleft()

            # create left child
            if result[index] != "N":
                node.left = TreeNode(int(result[index]))
                queue.append(node.left)
            index += 1
            
            # create right child
            if result[index] != "N":
                node.right = TreeNode(int(result[index]))
                queue.append(node.right)
            index += 1
        return root


        ## PREORDER DFS | time: O(n), space: O(n)
        # split str into result with comma
        result = data.split(",")
        self.index = 0

        def dfs():
            # if "N" -> null node
            if result[self.index] == "N":
                self.index += 1
                return None

            # otherwise value !!
            root = TreeNode(int(result[self.index]))
            self.index += 1

            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))