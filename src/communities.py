"""Community detection module"""

import networkx as nx
import community.community_louvain as community_louvain
from networkx.algorithms import community
import numpy as np


def louvain_communities(G):
    """
    Detect communities using the Louvain algorithm.
    
    Parameters:
    -----------
    G : networkx.Graph
        Input graph
        
    Returns:
    --------
    dict : Dictionary mapping node IDs to community assignments
    float : Modularity score
    """
    partition = community_louvain.best_partition(G)
    modularity = community_louvain.modularity(partition, G)
    
    return partition, modularity


def girvan_newman_communities(G, num_communities=2):
    """
    Detect communities using the Girvan-Newman algorithm.
    
    Parameters:
    -----------
    G : networkx.Graph
        Input graph
    num_communities : int
        Desired number of communities
        
    Returns:
    --------
    dict : Dictionary mapping node IDs to community assignments
    """
    # Create a copy to avoid modifying the original graph
    G_copy = G.copy()
    
    # Run Girvan-Newman algorithm
    communities_generator = community.girvan_newman(G_copy)
    
    # Get communities at the desired level
    communities = None
    for comm_tuple in communities_generator:
        if len(comm_tuple) >= num_communities:
            communities = comm_tuple
            if len(comm_tuple) == num_communities:
                break
    
    # If we didn't get exactly num_communities, use the last one we found
    if communities is None:
        # Fallback: start over and get the first partition
        G_copy = G.copy()
        communities_generator = community.girvan_newman(G_copy)
        communities = next(communities_generator)
    
    # Convert to dictionary format (handle frozensets from networkx)
    partition = {}
    comm_list = list(communities)  # Convert tuple to list
    for idx, comm in enumerate(comm_list[:num_communities]):
        for node in comm:
            partition[node] = idx
    
    # Handle any remaining nodes (assign to last community)
    for node in G.nodes():
        if node not in partition:
            partition[node] = num_communities - 1
    
    return partition


def compute_modularity(G, partition):
    """
    Compute modularity for a given partition.
    
    Parameters:
    -----------
    G : networkx.Graph
        Input graph
    partition : dict
        Dictionary mapping node IDs to community assignments
        
    Returns:
    --------
    float : Modularity score
    """
    return community_louvain.modularity(partition, G)


def get_community_members(partition, community_id):
    """
    Get all nodes belonging to a specific community.
    
    Parameters:
    -----------
    partition : dict
        Dictionary mapping node IDs to community assignments
    community_id : int
        Community ID to filter for
        
    Returns:
    --------
    list : List of node IDs in the specified community
    """
    return [node for node, comm in partition.items() if comm == community_id]


