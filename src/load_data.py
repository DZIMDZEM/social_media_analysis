"""Data loading module for Zachary Karate Club dataset"""

import networkx as nx
import json
import os


def load_from_edgelist(filepath='data/karate.edgelist'):
    """
    Load graph from edgelist file.
    
    Parameters:
    -----------
    filepath : str
        Path to the edgelist file
        
    Returns:
    --------
    networkx.Graph : Loaded graph
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Edgelist file not found: {filepath}")
    
    G = nx.read_edgelist(filepath, nodetype=int)
    return G


def load_from_networkx():
    """
    Load Zachary Karate Club graph directly from NetworkX.
    
    Returns:
    --------
    networkx.Graph : Zachary Karate Club graph
    """
    G = nx.karate_club_graph()
    return G


def load_metadata(filepath='data/metadata.json'):
    """
    Load dataset metadata.
    
    Parameters:
    -----------
    filepath : str
        Path to the metadata JSON file
        
    Returns:
    --------
    dict : Metadata dictionary
    """
    if not os.path.exists(filepath):
        return {}
    
    with open(filepath, 'r') as f:
        metadata = json.load(f)
    
    return metadata


def load_graph(source='networkx', filepath='data/karate.edgelist'):
    """
    Load the Zachary Karate Club graph from specified source.
    
    Parameters:
    -----------
    source : str
        Source to load from: 'networkx' or 'edgelist'
    filepath : str
        Path to edgelist file (if source is 'edgelist')
        
    Returns:
    --------
    networkx.Graph : Loaded graph
    dict : Metadata dictionary
    """
    if source == 'networkx':
        G = load_from_networkx()
    elif source == 'edgelist':
        G = load_from_edgelist(filepath)
    else:
        raise ValueError(f"Unknown source: {source}. Use 'networkx' or 'edgelist'")
    
    metadata = load_metadata()
    
    return G, metadata


