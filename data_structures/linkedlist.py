class Node:
	data = None
	next = None

	def __init__(self,data):
		self.data = data

	def set_next(self,next):
		self.next = next

	def set_data(self,data):
		self.data = data

	def to_str(self):
		return f"Node -> data: {self.data},next: {self.next}"

class LinkedList:
	# const: bad at searching things or get data by index,and it is much bigger than a array
	# pro: but it's fast to add and remove data of the head

	def __init__(self):
		self.head = None
		self.size = 0

	def is_empty(self):
		return self.head == None

	def push(self,data):
		last = self.get_value(self.size - 1)
		self.size += 1

		if last == None:
			self.head = Node(data)
			return

		new_node = Node(data)
		last.set_next(new_node)

	def add(self,data):
		self.size += 1

		new_node = Node(data)
		new_node.set_next(self.head)

		self.head = new_node

	def remove_by_index(self,index):
		current = self.head

		if index == 0:
			self.head = current.next
			return

		if index > self.size:
			return

		self.size -= 1

		for i in range(index - 1):
			current = current.next
		current.next = current.next.next
		return current

	def remove(self,key):
		self.remove_by_index(self.search(key))

	def insert(self,index,data):
		if index == 0:
			self.add(data)
			return

		if index > self.size:
			return

		self.size += 1
		current = self.get_value(index - 1)

		node = Node(data)
		node.set_next(current.next)
		current.next = node
		return current

	def search(self,key):
		count = 0
		current = self.head

		while current:
			print(current.data,self.head.data)
			if current.data == key:
				return count

			current = current.next
			count += 1

	def to_str(self):
		nodes = []
		current = self.head

		while current:
			nodes.append(f"{current.data}")
			current = current.next
		if nodes:
			return f"LinkedList -> {' >> '.join(nodes)}"
		return f"LinkedList -> None"

	def merge(self,left,right):
		l = LinkedList()
		i = 0
		k = 0

		while i < left.size and k < right.size:
			if left.get_value(i).data < right.get_value(k).data:
				l.push(left.get_value(i).data)
				i += 1
			else:
				l.push(right.get_value(k).data)
				k += 1

		while i < left.size:
			l.push(left.get_value(i).data)
			i += 1

		while k < right.size:
			l.push(right.get_value(k).data)
			k += 1

		return l

	def merge_sort(self):
		if self.size == 1 or self.head == None:
			return self
		
		split_list = self.split()

		left_half = split_list.head
		right_half = left_half.next

		left = left_half.data.merge_sort()
		right = right_half.data.merge_sort()

		return self.merge(left,right)

	def binary_search(self,target):
		first = 0
		last = self.size - 1

		while first <= last:
			midpoint = (first + last) // 2
			value = self.get_value(midpoint)

			if value.data == target:
				return midpoint

			if value.data < target:
				first = midpoint + 1
			else:
				last = midpoint - 1

		return None

	def get_value(self,index):
		if index == 0:
			return self.head

		current = self.head

		for i in range(index):
			current = current.next

		return current

	def slice(self,start,end):
		start_node = self.get_value(start)
		current = start_node

		l = LinkedList()

		for i in range(end - start):
			l.push(current.data)
			current = current.next
		
		return l

	def split(self):
		if self.head == None:
			return self

		l = LinkedList()

		l.add(self.slice(self.size // 2 + 1,self.size))
		l.add(self.slice(0, self.size // 2))

		return l
