class Node:
	def __init__(self, _data, _next = None, _prev = None):
		self._data = _data
		self._next = _next
		self._prev = _prev
		
class DoublyLinkedList:
	def __init__(self):
		self._head = None
		self._tail = None
		self._len = 0
	
	def head(self):
		if (self._len > 0): 
			return self._head._data 
		else:
			return None 
	
	def tail(self):
		if (self._len > 0): 
			return self._tail._data 
		else:
			return None 
		
	def add_first(self, item):
		
		new_node = Node(item, self._head, None)
		if len(self) != 0: self._head._prev = new_node
		self._head = new_node
		
		self._len += 1
		
		if len(self) == 1: self._tail = self._head
	
	def add_last(self, item):		
		new_node = Node(item, None, self._tail)
		if len(self) != 0: self._tail._next = new_node
		self._tail = new_node
		
		self._len += 1
		if len(self) == 1: self._head = self._tail

	def remove_first(self):
		if len(self) == 0: raise RuntimeError("attempt to remove_first from empty DLL")
		
		data = self._head._data
		if len(self) != 1: self._head._next._prev = None
		self._head = self._head._next
		
		self._len -= 1
		
		if len(self) == 0: self._tail = None
		
		return data

	
	def remove_last(self):
		if len(self) == 0: raise RuntimeError("attempt to remove_last from empty DLL")
		
		data = self._tail._data
		if len(self) != 1: self._tail._prev._next = None
		self._tail = self._tail._prev
		
		self._len -= 1
		
		if len(self) == 0: self._head = None
		
		return data

	def peek(self):
		return self._head._data

	def __len__(self):
		return self._len
