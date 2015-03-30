import searchtree
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

taxa = ["monkey", "human", "fish", "bird"]

def create_phylogeny():

	# Initialize phylogeny using first three taxa
	random.shuffle(taxa)
	print taxa
	T = UnrootedPhylogeny(len(taxa), 0, 1, 2)
	
	# Initialize search tree
	
create_phylogeny()
print quartet_query(x, a, b, c)