"""Centrality measures computation module"""

import networkx as nx
import pandas as pd


def compute_degree_centrality(G):
    """
    Compute degree centrality for all nodes.
    
    Parameters:
    -----------
    G : networkx.Graph
        Input graph
        
    Returns:
    --------
    dict : Dictionary mapping node IDs to degree centrality values
    """
    return nx.degree_centrality(G)


def compute_betweenness_centrality(G, normalized=True):
    """
    Compute betweenness centrality for all nodes.
    
    Parameters:
    -----------
    G : networkx.Graph
        Input graph
    normalized : bool
        Whether to normalize the centrality values
        
    Returns:
    --------
    dict : Dictionary mapping node IDs to betweenness centrality values
    """
    return nx.betweenness_centrality(G, normalized=normalized)


def compute_closeness_centrality(G):
    """
    Compute closeness centrality for all nodes.
    
    Parameters:
    -----------
    G : networkx.Graph
        Input graph
        
    Returns:
    --------
    dict : Dictionary mapping node IDs to closeness centrality values
    """
    return nx.closeness_centrality(G)


def compute_all_centralities(G):
    """
    Compute all centrality measures and return as a DataFrame.
    
    Parameters:
    -----------
    G : networkx.Graph
        Input graph
        
    Returns:
    --------
    pandas.DataFrame : DataFrame with node IDs and centrality measures
    """
    degree = compute_degree_centrality(G)
    betweenness = compute_betweenness_centrality(G)
    closeness = compute_closeness_centrality(G)
    
    df = pd.DataFrame({
        'node': list(degree.keys()),
        'degree_centrality': list(degree.values()),
        'betweenness_centrality': list(betweenness.values()),
        'closeness_centrality': list(closeness.values())
    })
    
    df = df.sort_values('node').reset_index(drop=True)
    
    return df


def get_top_central_nodes(centralities, n=5):
    """
    Get top N nodes by centrality measure.
    
    Parameters:
    -----------
    centralities : dict
        Dictionary of centrality values
    n : int
        Number of top nodes to return
        
    Returns:
    --------
    list : List of tuples (node_id, centrality_value) for top N nodes
    """
    sorted_nodes = sorted(centralities.items(), key=lambda x: x[1], reverse=True)
    return sorted_nodes[:n]


