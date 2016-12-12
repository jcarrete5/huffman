#
# huffman.py
# Demonstartes Huffman coding and decoding
# Created by: Jason R. Carrete
# Written with Python 3
#

from queue import PriorityQueue

class Node:
	def __init__(self, symbol, weight):
		self.parent = None
		self.left = None
		self.right = None
		self.symbol = symbol
		self.weight = weight

	def __lt__(self, other):
		return self.weight < other.weight

infile = open("input.txt", "r")
data = infile.read()
infile.close()

pQueue = PriorityQueue()
for ch in set(data):
	node = Node(ch, data.count(ch) / len(data))
	pQueue.put(node)
while not pQueue.empty():
	sym = pQueue.get().symbol
	print("********")
	print(sym + " : " + str(ord(sym)))
