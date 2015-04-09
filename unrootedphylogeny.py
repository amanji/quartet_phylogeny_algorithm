class UnrootedPhylogeny:

	def __init__(self, numtaxa, a, b, c):
		self.largestnodenum = numtaxa
		self.edges = []
		self.edges.append((self.largestnodenum, a))
		self.edges.append((self.largestnodenum, b))
		self.edges.append((self.largestnodenum, c))
		
	def insertLeaf(self, edgenum, leaf):
		self.largestnodenum += 1
		oldedge = self.edges[edgenum]
		
		# Edge from old internal node to new internal node
		self.edges[edgenum] = (oldedge[0], self.largestnodenum)
		# Edge from new internal node to old leaf
		self.edges.append((self.largestnodenum, oldedge[1]))
		# Edge from new internal node to new leaf
		self.edges.append((self.largestnodenum, leaf))
		
		# Return the ids of the new edges (in same order)
		return (edgenum, len(self.edges)-2, len(self.edges)-1)

	def getLargestNodeNum(self):
		return self.largestnodenum

	def printEdges(self):
		for edge in self.edges:
			print edge

	def getEdges(self):
		return self.edges