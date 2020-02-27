class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	# Function to print the list
	def printList(self):
		node = self
		output = ''
		while node != None:
			output += str(node.val)
			output += " "
			node = node.next
		print(output)

	# Iterative Solution
	def reverseIteratively(self, head):
		# Implement this.
		node = head
		previousNode = None
		nextNode = None
		while node is not None:
			# step to the next element
			nextNode = node.next
			# set the 'next' node to the last node
			node.next = previousNode
			# current node becomes previous
			previousNode = node
			# move to the next node
			node = nextNode

		return node

	# Recursive Solution
	def reverseRecursively(self, head):
		# Implement this.
		def reverse(node, previousNode = None):
			nextNode = node.next
			# set the 'next' node to the last node
			node.next = previousNode
			# if there's a next node, reverse it
			if nextNode:
				return reverse(nextNode, node)
			# otherwise return the original node
			else:
				return node

		return reverse(head)


# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
# testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4