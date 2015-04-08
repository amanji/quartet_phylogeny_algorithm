#!usr/bin/env python
from Bio import Phylo
from cStringIO import StringIO
import pylab

# Test script for printing out at tree:

# This is a good alternative to the PHYLIP program because:
# 1. It's old.
# 2. We can pipe our results directly to pythons functions rather than having to call up the PHYLIP program from command line

# So far the formats supported for this library are:
# newick
# nexus
# nexml
# phyloxml
# cdao

# The simplest format for our purposes will be newick


# An example output from our tree algorithm:

#If any number appears more than once then it is an internal node
# We already know that the taxa will be numbered from 0 to len(taxa)-1
# There fore all internal nodes begin at len(taxa) and go up from there

#(0, 6)
#(1, 7)
#(2, 6)
#(7, 6)
#(7, 8)
#(8, 3)
#(8, 9)
#(9, 4)
#(9, 5)

# If one of the two numbers in any of the tuples appears in any other tuple then it is an internal node
# Other wise it is a leaf

tree_data = '((L4,L5)9, ((L3)8, ((L1)7, (L0,L2)6)))'
handle = StringIO(tree_data)
tree = Phylo.read(handle, "newick")

# Alternatively this can be read in one line as:
# tree = Phylo.read(StringIO("(A, (B, C), (D, E))"), "newick")

tree.ladderize()   # Flip branches so deeper clades are displayed at top
Phylo.draw(tree)

#Phylo.draw_graphviz(tree, node_size=100)
#pylab.show()