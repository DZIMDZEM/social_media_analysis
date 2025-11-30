"""Helper utility functions for network analysis"""

import numpy as np
import pandas as pd
import networkx as nx


def get_node_attributes(G, attribute_name):
    """
    Extract node attributes as a dictionary.
    
    Parameters:
    -----------
    G : networkx.Graph
        Input graph
    attribute_name : str
        Name of the node attribute to extract
        
    Returns:
    --------
    dict : Dictionary mapping node IDs to attribute values
    """
    return nx.get_node_attributes(G, attribute_name)


def attribute_to_numeric(attributes, mapping=None):
    """
    Convert categorical attributes to numeric values.
    
    Parameters:
    -----------
    attributes : dict
        Dictionary of node attributes
    mapping : dict, optional
        Custom mapping from categories to numbers
        
    Returns:
    --------
    dict : Dictionary mapping node IDs to numeric values
    """
    unique_vals = set(attributes.values())
    
    if mapping is None:
        mapping = {val: idx for idx, val in enumerate(sorted(unique_vals))}
    
    return {node: mapping[val] for node, val in attributes.items()}


def get_adjacency_matrix(G, nodes=None):
    """
    Get adjacency matrix of the graph.
    
    Parameters:
    -----------
    G : networkx.Graph
        Input graph
    nodes : list, optional
        Ordered list of nodes (if None, uses sorted node list)
        
    Returns:
    --------
    numpy.ndarray : Adjacency matrix
    list : Ordered list of nodes
    """
    if nodes is None:
        nodes = sorted(G.nodes())
    
    return nx.adjacency_matrix(G, nodelist=nodes).toarray(), nodes


def normalize_dict(d):
    """
    Normalize a dictionary of numeric values to [0, 1] range.
    
    Parameters:
    -----------
    d : dict
        Dictionary with numeric values
        
    Returns:
    --------
    dict : Normalized dictionary
    """
    values = np.array(list(d.values()))
    min_val = values.min()
    max_val = values.max()
    
    if max_val == min_val:
        return {k: 0.5 for k in d.keys()}
    
    return {k: (v - min_val) / (max_val - min_val) for k, v in d.items()}


