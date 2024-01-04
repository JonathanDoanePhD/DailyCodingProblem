class Node:
	def __init__(self, data):
		self.data = data
		self.both = 0 # This will hold the XOR of the next and previous node IDs

class XORLinkedList:
	def __init__(self):
		self.head = self.tail = None
		# Dictionary to store Node objects by their IDs. This is necessary because Python doesn't
		# provide direct access to objects based on memory location.
		self.nodes = {} 

	def _xor(self, a, b):
		"""Helper function to get the XOR of two IDs."""
		return a ^ b

	def insert_at_head(self, data):
		"""Inserts a new node with the provided data at the head of the list."""
		new_node = Node(data)
		new_id = id(new_node)
		self.nodes[new_id] = new_node
		
		if self.head:
			# Adjusting both values for new node and existing head
			new_node.both = self._xor(0, id(self.head))
			self.head.both = self._xor(new_node.both, id(self.head))
		else:
			# If list is empty, the new node becomes the tail
			self.tail = new_node
		self.head = new_node

	def insert_at_tail(self, data):
		"""Inserts a new node with the provided data at the tail of the list."""
		new_node = Node(data)
		new_id = id(new_node)
		self.nodes[new_id] = new_node
		
		if self.tail:
			# Adjusting both values for new node and existing tail
			new_node.both = self._xor(id(self.tail), 0)
			self.tail.both = self._xor(new_node.both, id(self.tail))
		else:
			# If list is empty, the new node becomes the head
			self.head = new_node
		self.tail = new_node

	def delete_from_head(self):
		"""Deletes the head node from the list."""
		if self.head:
			# If there's a next node after the head, update its both value
			next_node_id = self._xor(0, self.head.both)
			next_node = self.nodes.get(next_node_id) if next_node_id else None
			
			if next_node:
				next_node.both = self._xor(id(self.head), next_node.both)
			else:
				self.tail = None
			
			# Remove the current head from the nodes dictionary and update the head pointer
			del self.nodes[id(self.head)]
			self.head = next_node

	def delete_from_tail(self):
		"""Deletes the tail node from the list."""
		if self.tail:
			# If there's a previous node before the tail, update its both value
			prev_node_id = self._xor(self.tail.both, 0)
			prev_node = self.nodes.get(prev_node_id) if prev_node_id else None
			
			if prev_node:
				prev_node.both = self._xor(id(self.tail), prev_node.both)
			else:
				self.head = None
			
			# Remove the current tail from the nodes dictionary and update the tail pointer
			del self.nodes[id(self.tail)]
			self.tail = prev_node

	def print_list(self):
		"""Prints the entire list from head to tail."""
		current = self.head
		prev_id = 0
		while current:
			print(current.data, end=" ")
			# Compute the ID of the next node
			next_id = self._xor(prev_id, current.both)
			
			# Move the pointers
			prev_id = id(current)
			current = self.nodes.get(next_id)
		print()

if __name__ == '__main__':
	list_ = XORLinkedList()
	list_.insert_at_head(10)
	list_.insert_at_head(20)
	list_.insert_at_tail(30)
	list_.insert_at_tail(40)
	list_.print_list() # Expected: 20 10 30 40
	list_.delete_from_head()
	list_.print_list() # Expected: 10 30 40
	list_.delete_from_tail()
	list_.print_list() # Expected: 10 30

	# This Code Is Contributed By Shubham Tiwari
