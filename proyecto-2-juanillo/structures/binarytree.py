from __future__ import annotations
from typing import TypeVar, Generic, Literal

T = TypeVar('T')


class Node(Generic[T]):
	def __init__(self, data):
		self.data = data
		self.left: Node | None = None
		self.right: Node | None = None

	def is_leaf(self) -> bool:
		return self.left is None and self.right is None

	def has_children(self) -> Literal['left', 'right', 'both', 'None']:
		if self.left is None and self.right is None:
			return  'None'
		elif self.left is not None and self.right is not None:
			return 'both'
		elif self.left is not None and self.right is None:
			return 'left'
		else:
			return 'right'

class BinaryTree(Generic[T]):
	def __init__(self):
		self.root: Node | None = None

	def insert_left(self, data: T, ref: T|None = None):
		if ref is None:
			new_node = Node(data)
			self.root = new_node
		else:
			node = self.search(self.root, ref)
			if node is not None:
				new_node = Node(data)
				node.left = new_node
			else:
				raise Exception('Elemento no encontrado')

	def insert_right(self, data: T, ref: T|None = None):
		if ref is None:
			new_node = Node(data)
			self.root = new_node
		else:
			node = self.search(self.root, ref)
			if node is not None:
				new_node = Node(data)
				node.right = new_node
			else:
				raise Exception('Elemento no encontrado')

	def search(self, subtree: Node[T] | None, ref:T) -> Node | None:

		if subtree is None:
			return None
		else:
			value = subtree.data
			if value == ref:
				return subtree

			node = self.search(subtree.left, ref)

			if node is not None:
				return node

			node = self.search(subtree.right, ref)
			return node

	def get_depth(self) -> int:
		def _get_depth(node: Node[T] | None) -> int:
			if node is None:
				return 0
			else:
				left_depth = _get_depth(node.left)
				right_depth = _get_depth(node.right)
				return max(left_depth, right_depth) + 1

		return _get_depth(self.root)

	def size(self) -> int:
		return self.__size(self.root)

	def __size(self, subtree: Node[T] | None) -> int:
		if subtree is None:
			return 0
		else:
			return 1 + self.__size(subtree.left) + self.__size(subtree.right)

	def get_root(self):
		if self.root is None:
			return None
		else:
			return self.root.data