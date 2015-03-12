class SearchTree:
	def __init__(self,rootid):
		self.left = None
		self.middle = None
		self.right = None
		self.leftlist = []
		self.middlelist = []
		self.rightlist = []
	
	def getLeftChild(self):
		return self.left
	def getMiddleChild(self):
		return self.middle
	def getRightChild(self):
		return self.right
		
	def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
            
    def insertMiddle(self,newNode):
        if self.middle == None:
            self.middle = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.middle = self.middle
            self.middle = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left