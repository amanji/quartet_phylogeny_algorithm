class SearchTree:
	def __init__(self, rootid, subtree_edges):
		self.left = None
		self.middle = None
		self.right = None
		self.leftlist = []
		self.middlelist = []
		self.rightlist = []
		self.rootid = rootid
		self.subtree_edges = subtree_edges
	
	def getLeftChild(self):
		return self.left
	def getMiddleChild(self):
		return self.middle
	def getRightChild(self):
		return self.right
	def getNodeValue(self):
		return self.rootid
	def setRootId(self, rootid):
		self.rootid = rootid
		
	def insertRight(self,newNode):
		if self.right == None:
			self.right = SearchTree(newNode, [])
		else:
			tree = SearchTree(newNode)
			tree.right = self.right
			self.right = tree
            
	def insertMiddle(self,newNode):
		if self.middle == None:
			self.middle = SearchTree(newNode, [])
		else:
			tree = SearchTree(newNode)
			tree.middle = self.middle
			self.middle = tree

	def insertLeft(self,newNode):
		if self.left == None:
			self.left = SearchTree(newNode, [])
		else:
			tree = SearchTree(newNode)
			self.left = tree
			tree.left = self.left
            
	def setLeftList(self, leftList):
		self.leftlist = leftList
			
	def setMiddleList(self, middleList):
		self.middlelist = middleList

	def setRightList(self, rightList):
		self.rightlist = rightList
       
	def printTree(self):
		if self != None:
			leftc = self.getLeftChild()
			middlec = self.getMiddleChild()
			rightc = self.getRightChild()
			if not (leftc or middlec or rightc):
				print "leaf:", self.getNodeValue()
			else:
				print "internal node:", self.getNodeValue()
				# print lists
				print "    left list: ", self.leftlist, " middle list: ", self.middlelist, " right list: ", self.rightlist
				print "    subtree edges: ", self.subtree_edges
			
			# print children
			if (leftc != None):
				leftc.printTree()
			if (middlec != None):
				middlec.printTree()
			if (rightc != None):
				rightc.printTree()