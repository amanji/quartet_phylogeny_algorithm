#!usr/bin/env python
from Bio import Phylo
from cStringIO import StringIO
import pylab

class TreePrinter:
  """
  Prints out a formatted tree using Phylo from BioPython.

  Instantiate a the printer by passing in a list of edges (tuple of number pairs) in the final unrooted tree,
  The number of taxa in the final tree,
  A dictionary of leaf number keys, and taxa id values

  Converts the list of tuples into a valid Newick string.

  Example:

  edges = [(0, 6),(1, 7),(2, 6),(7, 6),(7, 8),(8, 3),(8, 9),(9, 4),(9, 5)]

  newick = '((4,5)9, ((3)8, ((1)7, (0,2)6)))'
  """
  def __init__(self, edges, num_taxa):
    self.edges = edges
    self.num_taxa = num_taxa
    #self.taxa_labels = taxa_labels
    self.leaf_nodes = {}
    self.internal_nodes = []

    # Prepare dictionary of leaf nodes
    # Prepare list of connected internal nodes
    for edge in self.edges:
      if edge[0] < num_taxa:
        if edge[1] in self.leaf_nodes:
          self.leaf_nodes[edge[1]].append(edge[0])
        else:
          self.leaf_nodes[edge[1]] = [edge[0]]
      elif edge[1] < num_taxa:
        if edge[0] in self.leaf_nodes:
          self.leaf_nodes[edge[0]].append(edge[1])
        else:
          self.leaf_nodes[edge[0]] = [edge[1]]
      else:
        self.internal_nodes.append(edge)

    #Find the first parent with two leaves
    # NOTE: This approach will fail if theres only one taxa sequence
    #       the algorithm assumes at least two sequences
    first_leaf_node = 1
    for edge, leaves in self.leaf_nodes.iteritems():
       if len(leaves) > 1:
         first_leaf_node = edge
         break
    #print first_leaf_node

    # Prepare the newick string:
    #newick_str = str(tuple(self.leaf_nodes[first_leaf_node])) + str(first_leaf_node)
    newick_str = '(' + ",".join(map(str, self.leaf_nodes[first_leaf_node])) + ')' + str(first_leaf_node)

    print newick_str

    # Some of Pythons list functions dont allow lists to be mutated
    #   so this is a workaround
    internal_nodes_copy = self.internal_nodes[:]
    added = 0
    while(len(self.internal_nodes) > 0):
      for edge in self.internal_nodes:
        if edge[0] == first_leaf_node:
          first_leaf_node = edge[1]
          newick_str += ',(' + '(' + ",".join(map(str, self.leaf_nodes[first_leaf_node])) + ')' + str(first_leaf_node)
          added += 1
          internal_nodes_copy.remove(edge)
          self.internal_nodes = internal_nodes_copy[:]
        elif edge[1] == first_leaf_node:
          first_leaf_node = edge[0]
          newick_str += ',(' + '(' + ",".join(map(str, self.leaf_nodes[first_leaf_node])) + ')' + str(first_leaf_node)
          added += 1
          internal_nodes_copy.remove(edge)
          self.internal_nodes = internal_nodes_copy[:]
        else:
          continue
    
    newick_str += ')' * added
    #print newick_str    
    tree = Phylo.read(StringIO(newick_str), "newick")
    Phylo.draw(tree)