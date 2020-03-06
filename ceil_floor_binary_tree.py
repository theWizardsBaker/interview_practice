class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  # Fill this in.
  if root_node is None:
    return (floor, ceil)
  # if we match the value, we've found it
  elif root_node.value == k:
    return (k, k)
  elif root_node.value < k:
    # move right
    return findCeilingFloor(root_node.right, k, floor, root_node.value)
  elif root_node.value > k:
    # move left
    return findCeilingFloor(root_node.left, k, root_node.value, ceil)



root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print findCeilingFloor(root, 5)


root = Node(9)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(11)
root.right.right = Node(14)

print findCeilingFloor(root, 10)