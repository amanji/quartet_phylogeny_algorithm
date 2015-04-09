#!usr/bin/env python
from Bio import Phylo
from cStringIO import StringIO
import pylab

tree_data = '((L4,L5)9, ((L3)8, ((L1)7, (L0,L2)6)))'
handle = StringIO(tree_data)
tree = Phylo.read(handle, "newick")

tree.ladderize()   # Flip branches so deeper clades are displayed at top
Phylo.draw(tree)