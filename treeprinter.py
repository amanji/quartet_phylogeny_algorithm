#!usr/bin/env python
from Bio import Phylo
from cStringIO import StringIO
#import pylab
import graphviz as gv


class TreePrinter:
  """
  Prints out a formatted tree using Graphviz.

  Instantiate a the printer by passing in a list of edges (tuple of number pairs) in the final unrooted tree,
  The number of taxa in the final tree,
  A list of taxa that is the same length as the list of sequences
  """
  def __init__(self, edges, num_taxa, sequences, taxa_labels):
    self.edges = edges
    self.num_taxa = num_taxa
    self.sequences = sequences
    self.taxa_labels = taxa_labels
    self.leaf_nodes = {}
    self.internal_nodes = []
    self.bridging_nodes = []

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


    # It looks like dotgraph may be our best bet given our tree output
    # Need to format the tree properly
    dot = gv.Graph(comment='Quartet Phylogeny', format='pdf')
    for node, leaves in self.leaf_nodes.iteritems():
      #Create node
      parent = str(node)
      dot.node(parent, label="")

      for leaf in leaves:
        leaf = self.taxa_labels[leaf] + '_' + str(leaf)
        dot.node(leaf, shape="plaintext")
        dot.edge(parent, leaf)

    for edge_pair in self.internal_nodes:
      dot.edge(str(edge_pair[0]), str(edge_pair[1]))

    
    #Apply styling to the graph so it looks like a tree
    styles = {
        'graph': {
            'overlap' : 'false',
            'splines' : 'line',
            #'nodesep' : '0',
            #'label': 'A Fancy Graph',
            #'fontsize': '16',
            'rankdir': 'BT',
        },
        'nodes': {
            'fontname': 'Droid Sans',
            'shape': 'point',
            'fontcolor': 'black',
        },
        'edges': {
            'tailclip' : 'false',
            #'fontname': 'Courier',
            #'fontsize': '12',
        }
    }

    dot = self.apply_styles(dot,styles)
    dot.render('stx2', view=True)

  def apply_styles(self, graph, styles):
    graph.graph_attr.update(
      ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
      ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
      ('edges' in styles and styles['edges']) or {}
    )
    return graph


