"""Node attribute-based clustering module"""

import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import pandas as pd


def prepare_node_features(G, centralities_df, attributes=None):
    """
    Prepare node feature matrix for clustering.
    
    Parameters:
    -----------
    G : networkx.Graph
        Input graph
    centralities_df : pandas.DataFrame
        DataFrame with centrality measures
    attributes : dict, optional
        Dictionary of additional node attributes
        
    Returns:
    --------
    numpy.ndarray : Feature matrix (nodes x features)
    list : Ordered list of node IDs
    """
    # Start with centrality measures
    features = centralities_df[['degree_centrality', 'betweenness_centrality', 
                                 'closeness_centrality']].values
    
    # Add additional attributes if provided
    if attributes:
        node_list = centralities_df['node'].tolist()
        attr_values = np.array([attributes.get(node, 0) for node in node_list])
        features = np.column_stack([features, attr_values])
    
    return features, centralities_df['node'].tolist()


def kmeans_clustering(features, n_clusters=2, random_state=42):
    """
    Perform KMeans clustering on node features.
    
    Parameters:
    -----------
    features : numpy.ndarray
        Feature matrix
    n_clusters : int
        Number of clusters
    random_state : int
        Random seed for reproducibility
        
    Returns:
    --------
    numpy.ndarray : Cluster assignments
    sklearn.cluster.KMeans : Fitted KMeans model
    """
    # Standardize features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    # Perform KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    labels = kmeans.fit_predict(features_scaled)
    
    return labels, kmeans


def hierarchical_clustering(features, n_clusters=2, linkage='ward'):
    """
    Perform hierarchical clustering on node features.
    
    Parameters:
    -----------
    features : numpy.ndarray
        Feature matrix
    n_clusters : int
        Number of clusters
    linkage : str
        Linkage criterion ('ward', 'complete', 'average')
        
    Returns:
    --------
    numpy.ndarray : Cluster assignments
    """
    # Standardize features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    # Perform hierarchical clustering
    clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
    labels = clustering.fit_predict(features_scaled)
    
    return labels


def create_clustering_dict(node_list, labels):
    """
    Create a dictionary mapping node IDs to cluster assignments.
    
    Parameters:
    -----------
    node_list : list
        List of node IDs
    labels : numpy.ndarray
        Cluster labels
        
    Returns:
    --------
    dict : Dictionary mapping node IDs to cluster IDs
    """
    return {node: int(cluster) for node, cluster in zip(node_list, labels)}

