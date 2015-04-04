class UnrootedPhylogeny:

	def __init__(self, numtaxa, a, b, c):
		self.largestnodenum = numtaxa
		self.edges = []
		self.edges.append((a, self.largestnodenum))
		self.edges.append((b, self.largestnodenum))
		self.edges.append((c, self.largestnodenum))
		
	def insertLeaf(self, edgenum, leaf):
		self.largestnodenum += 1
		oldedge = self.edges[edgenum]
		self.edges[edgenum] = (oldedge[0], self.largestnodenum)
		self.edges.append((self.largestnodenum, oldedge[1]))
		self.edges.append((self.largestnodenum, leaf))
		# Return the ids of the new edges
		return (edgenum, len(self.edges)-1, len(self.edges)-2)

	def getLargestNodeNum(self):
		return self.largestnodenum

	def printEdges(self):
		for edge in self.edges:
			print edge