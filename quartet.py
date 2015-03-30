import searchtree
from Bio import SeqIO
from Bio import AlignIO
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq

a = SeqRecord(Seq("AAAACGT", generic_dna), id="Alpha")
b = SeqRecord(Seq("AAA-CGT", generic_dna), id="Beta")
c = SeqRecord(Seq("AAAAGGT", generic_dna), id="Gamma")
align = MultipleSeqAlignment([a, b, c], annotations={"tool": "demo"})
print(align)


# Determine which topology of the four nodes is most likely
def quartet_query(x, a1, a2, a3, msa):

	
# Determine which subtree of internal node v we should add x to
def node_query(T, v, x):