# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def isValidBST(self, root):


node = TreeNode(5)
node.left = TreeNode(4)
node.right = TreeNode(7)
print(Solution().isValidBST(node))

# Tree 1
node = TreeNode(5)
node.left = TreeNode(1)
node.right = TreeNode(4)
node.right.left = TreeNode(3)
node.right.right = TreeNode(6)

# Tree 2
node2 = TreeNode(5)
node2.left = TreeNode(1)
node2.right = TreeNode(6)
node2.right.left = TreeNode(4)
node2.right.right = TreeNode(7)

# Tree 3
node3 = TreeNode(5)
node3.left = TreeNode(1)
node3.right = TreeNode(6)
node3.right.left = TreeNode(7)
node3.right.right = TreeNode(8)

# Tree 4
node4 = TreeNode(5)
node4.left = TreeNode(1)
node4.right = TreeNode(7)
node4.right.left = TreeNode(6)
node4.right.right = TreeNode(8)

print("Node 1",Solution().isValidBST(node))
print("Node 2",Solution().isValidBST(node2))
print("Node 3",Solution().isValidBST(node3))
print("Node 4",Solution().isValidBST(node4))
# True