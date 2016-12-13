#
# huffman.py
# Demonstartes Huffman coding and decoding
# Created by: Jason R. Carrete
# Written with Python 3
#

from queue import PriorityQueue
from queue import Queue

class Node:
	def __init__(self, symbol, weight):
		self.parent = None
		self.left = None
		self.right = None
		self.symbol = symbol
		self.weight = weight

	def __lt__(self, other):
		return self.weight < other.weight

	def __str__(self):
		return "ASCII: " + str(ord(self.symbol)) + "\nWeight: " + str(self.weight)

with open("input.txt", "r") as infile:
	data = infile.read()

pQueue = PriorityQueue()
for ch in set(data):
	node = Node(ch, data.count(ch))
	pQueue.put(node)

while pQueue.qsize() > 1:
	n1 = pQueue.get()
	n2 = pQueue.get()

	internal = Node('\0', n1.weight + n2.weight)
	n1.parent = internal
	n2.parent = internal
	internal.left = n1
	internal.right = n2

	pQueue.put(internal)

root = pQueue.get()

buf = Queue()
buf.put(root)
# traverse the binary tree using Level Order Traversal
while not buf.empty():
	node = buf.get()
	print(str(node) + "\n")

	if node.left is not None:
		buf.put(node.left)
	if node.right is not None:
		buf.put(node.right)
