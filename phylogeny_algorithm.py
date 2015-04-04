from searchtree import SearchTree
from quartet import quartet_query
from unrootedphylogeny import UnrootedPhylogeny
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

sequences = ["A-CGG", "AACGT", "A-CGT", "AAGGT", "CAGGT", "CAGAT"]
#sequences = ["A-CGG", "AACGT", "A-CGT", "AAGGT"]

taxa = ["monkey", "human", "fish", "bird"]

def create_phylogeny():

	# Initialize phylogeny using first three taxa
	#random.shuffle(taxa)
	#print taxa
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
			# Perform the quartet query
			othertaxa = [Y.leftlist[0], Y.middlelist[0], Y.rightlist[0]]
			idx = quartet_query(sequences[i], sequences[othertaxa[0]], sequences[othertaxa[1]], sequences[othertaxa[2]])
			if idx == 0:
				YTi = YTi.left
			elif idx == 1:
				YTi = YTi.middle
			else:
				YTi = YTi.right
		
		# Split the edge in the phylogeny to add the new taxon
		newedges = T.insertLeaf(YTi.rootid, i)
		
		# Add the new edges to the search tree
		YTi.insertLeft(newedges[0])
		YTi.insertMiddle(newedges[1])
		YTi.insertRight(newedges[2])
		
		# Update rootid of YTi
		YTi.setRootId(T.getLargestNodeNum())
		
		# Update the lists in the leaf of the search tree
		closesttaxon = othertaxa[idx]
		othertaxa.remove(closesttaxon)
		# Left list gets just-added taxon
		YTi.setLeftList([i])
		# Middle list and right list get the closest taxon plus one of the other ones
		# from the quartet query (arbitrarily assigned to 0 and 1)
		YTi.setMiddleList([closesttaxon, othertaxa[0]])
		YTi.setRightList([closesttaxon, othertaxa[1]])
		
	return T
	
tree = create_phylogeny()
tree.printEdges()