import searchtree
import quartet
from unrootedphylogeny import UnrootedPhylogeny
import random

taxa = ["monkey", "human", "fish", "bird"]

def create_phylogeny():

	# Initialize phylogeny using first three taxa
	random.shuffle(taxa)
	print taxa
	T = UnrootedPhylogeny(len(taxa), 0, 1, 2)
	
	# Initialize search tree
	
create_phylogeny()