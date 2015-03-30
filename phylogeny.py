class Phylogeny:
	def __init__(self,rootid):
		self.left = None
		self.right = None
		self.rootid = rootid
	
	def getLeftChild(self):
		return self.left
	def getRightChild(self):
		return self.right
	def getNodeValue(self):
		return self.rootid
		
	def insertRight(self,newNode):
        if self.right == None:
            self.right = Phylogeny(newNode)
        else:
            tree = Phylogeny(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = Phylogeny(newNode)
        else:
            tree = Phylogeny(newNode)
            self.left = tree
            tree.left = self.left
            
    def printTree(self):
        if self != None:
            print(self.getNodeValue())
            printTree(self.getLeftChild())
            printTree(self.getRightChild())
