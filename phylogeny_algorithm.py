from searchtree import SearchTree
from quartet import quartet_query
from unrootedphylogeny import UnrootedPhylogeny
from treeprinter import TreePrinter
import random
from Bio import SeqIO
from Bio import AlignIO
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq

# x = SeqRecord(Seq("A-CGG", generic_dna), id="bla")
# a = SeqRecord(Seq("AACGT", generic_dna), id="Alpha")
# b = SeqRecord(Seq("A-CGT", generic_dna), id="Beta")
# c = SeqRecord(Seq("AAGGT", generic_dna), id="Gamma")
# align = MultipleSeqAlignment([a, b, c], annotations={"tool": "demo"})
# print(align)

x = Seq("A-CGG", generic_dna)
a = Seq("AACGT", generic_dna)
b = Seq("A-CGT", generic_dna)
c = Seq("AAGGT", generic_dna)

#sequences = ["A-CGG", "AACGT", "A-CGT", "AAGGT", "CAGGT", "CAGAT", "A-CGG", "AACGT", "A-CGT", "AAGGT", "CAGGT", "CAGAT"]
sequences = ["A-CGG", "AACGT", "A-CGT", "AAGGT", "CAGGT", "CAGGT", "AAGGT"]
taxa = list(range(1,len(sequences)+1))

def create_phylogeny():

	# Initialize phylogeny using first three taxa
	#random.shuffle(sequences)
	#print sequences
	first_internal_node = len(sequences)
	T = UnrootedPhylogeny(first_internal_node, 0, 1, 2)
	
	# Initialize search tree
	Y = SearchTree(first_internal_node, T.edges)
	Y.setLeftList([0])
	Y.setMiddleList([1])
	Y.setRightList([2])
	Y.insertLeft(0)
	Y.insertMiddle(1)
	Y.insertRight(2)
	
	# Insert each taxon into the phylogeny
	for i in range(3,len(sequences)):
		print "====================================================="
		print "i:", i
		print "Search tree:"
		Y.printTree()
		print "Phylogeny:"
		T.printEdges()
		YTi = Y
		
		# Move down the search tree until we get to a leaf
		while YTi.left or YTi.middle or YTi.right:
			print "Move down search tree... YTi:", YTi.rootid
			YTi.printTree()
			# Perform the quartet query
			othertaxa = [YTi.leftlist[0], YTi.middlelist[0], YTi.rightlist[0]]
			print "quartet query: ", othertaxa
			idx = quartet_query(sequences[i], sequences[othertaxa[0]], sequences[othertaxa[1]], sequences[othertaxa[2]])
			print "closest: ", othertaxa[idx]
			print "idx: ", idx
			if idx == 0:
				YTi = YTi.left
			elif idx == 1:
				YTi = YTi.middle
			else:
				YTi = YTi.right
		
		print "Last search tree:"
		YTi.printTree()
		# Split the edge in the phylogeny to add the new taxon
		print "Insert leaf... ", YTi.rootid
		newedges = T.insertLeaf(YTi.rootid, i)
		
		# Add the new edges to the search tree
		YTi.insertLeft(newedges[2]) # edge to new taxon (leaf)
		YTi.insertMiddle(newedges[1]) # edge to closest taxon (leaf)
		YTi.insertRight(newedges[0]) # edge to internal node
		
		# Update rootid of YTi
		YTi.setRootId(T.getLargestNodeNum())
		
		# Update the lists in the leaf of the search tree
		closesttaxon = othertaxa[idx]
		othertaxa.remove(closesttaxon)
		# Left list gets just-added taxon
		YTi.setLeftList([i])
		# Middle list gets closest taxon
		YTi.setMiddleList([closesttaxon])
		# Right list gets one of the other taxa
		YTi.setRightList([othertaxa[0]])
		
	return T
	
tree = create_phylogeny()
tree.printEdges()
treeprinter = TreePrinter(tree.getEdges(), len(sequences), sequences, taxa)
#print treeprinter.edges
#print treeprinter.num_taxa
#print treeprinter.leaf_nodes
#print treeprinter.internal_nodes