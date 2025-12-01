"""Network visualization and dimensionality reduction module"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from sklearn.manifold import MDS, TSNE
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns


def plot_network(G, node_colors=None, node_sizes=None, title="Network Graph",
                  pos=None, ax=None, highlight_nodes=None, edge_color='gray',
                  node_labels=False, figsize=(12, 8)):
    """
    Plot network graph with customizable node colors and sizes.
    
    Parameters:
    -----------
    G : networkx.Graph
        Input graph
    node_colors : dict or list, optional
        Node colors (dict mapping node to color, or list of colors)
    node_sizes : dict or list, optional
        Node sizes (dict mapping node to size, or list of sizes)
    title : str
        Plot title
    pos : dict, optional
        Node positions (if None, uses spring layout)
    ax : matplotlib.axes, optional
        Axes to plot on
    highlight_nodes : list, optional
        Nodes to highlight with border
    edge_color : str
        Color for edges
    node_labels : bool
        Whether to show node labels
    figsize : tuple
        Figure size
        
    Returns:
    --------
    matplotlib.figure.Figure : Figure object
    matplotlib.axes.Axes : Axes object
    dict : Node positions
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure
    
    # Compute layout if not provided
    if pos is None:
        pos = nx.spring_layout(G, k=1, iterations=50, seed=42)
    
    # Prepare node colors
    if node_colors is None:
        colors = ['lightblue'] * G.number_of_nodes()
    elif isinstance(node_colors, dict):
        node_list = sorted(G.nodes())
        colors = [node_colors.get(node, 'lightgray') for node in node_list]
    else:
        colors = node_colors
    
    # Prepare node sizes
    if node_sizes is None:
        sizes = [300] * G.number_of_nodes()
    elif isinstance(node_sizes, dict):
        node_list = sorted(G.nodes())
        sizes = [node_sizes.get(node, 300) for node in node_list]
    else:
        sizes = node_sizes
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, alpha=0.5, edge_color=edge_color, ax=ax)
    
    # Draw nodes
    node_list = sorted(G.nodes())
    nx.draw_networkx_nodes(G, pos, nodelist=node_list, node_color=colors,
                           node_size=sizes, alpha=0.9, ax=ax)
    
    # Highlight specific nodes
    if highlight_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=highlight_nodes,
                               node_color='red', node_size=[sizes[node_list.index(n)] * 1.5 
                                                            for n in highlight_nodes],
                               alpha=0.8, ax=ax, linewidths=3, edgecolors='darkred')
    
    # Draw labels
    if node_labels:
        labels = {node: node for node in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels, font_size=8, ax=ax)
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    return fig, ax, pos


def plot_by_communities(G, partition, title="Network by Communities", pos=None, ax=None):
    """
    Plot network colored by community assignment.
    
    Parameters:
    -----------
    G : networkx.Graph
        Input graph
    partition : dict
        Dictionary mapping node IDs to community assignments
    title : str
        Plot title
    pos : dict, optional
        Node positions
    ax : matplotlib.axes, optional
        Axes to plot on
        
    Returns:
    --------
    matplotlib.figure.Figure : Figure object
    matplotlib.axes.Axes : Axes object
    dict : Node positions
    """
    # Create color palette
    num_communities = len(set(partition.values()))
    palette = plt.cm.Set3(np.linspace(0, 1, num_communities))
    
    node_colors = {node: palette[comm % len(palette)] 
                   for node, comm in partition.items()}
    
    return plot_network(G, node_colors=node_colors, title=title, pos=pos, ax=ax)


def plot_centrality_heatmap(G, centralities_dict, title="Centrality Heatmap", ax=None):
    """
    Plot heatmap of centrality measures.
    
    Parameters:
    -----------
    G : networkx.Graph
        Input graph
    centralities_dict : dict
        Dictionary of centrality measures (dict of dicts)
    title : str
        Plot title
    ax : matplotlib.axes, optional
        Axes to plot on
        
    Returns:
    --------
    matplotlib.figure.Figure : Figure object
    matplotlib.axes.Axes : Axes object
    """
    import pandas as pd
    
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 8))
    else:
        fig = ax.figure
    
    # Prepare data
    df = pd.DataFrame(centralities_dict)
    df = df.sort_index()
    
    # Plot heatmap
    sns.heatmap(df.T, annot=True, fmt='.3f', cmap='YlOrRd', ax=ax, 
                cbar_kws={'label': 'Centrality Value'})
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Node ID', fontsize=12)
    ax.set_ylabel('Centrality Measure', fontsize=12)
    
    plt.tight_layout()
    return fig, ax


def compute_pca_embedding(features, n_components=2, random_state=42):
    """
    Compute PCA embedding of node features.
    
    Parameters:
    -----------
    features : numpy.ndarray
        Feature matrix
    n_components : int
        Number of dimensions
    random_state : int
        Random seed (for consistency, though PCA is deterministic)
        
    Returns:
    --------
    numpy.ndarray : Embedded coordinates
    sklearn.decomposition.PCA : Fitted PCA model
    """
    # Standardize features for PCA
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    # Compute PCA
    pca = PCA(n_components=n_components, random_state=random_state)
    embedding = pca.fit_transform(features_scaled)
    return embedding, pca


def compute_mds_embedding(features, n_components=2, random_state=42):
    """
    Compute MDS embedding of node features.
    
    Parameters:
    -----------
    features : numpy.ndarray
        Feature matrix
    n_components : int
        Number of dimensions
    random_state : int
        Random seed
        
    Returns:
    --------
    numpy.ndarray : Embedded coordinates
    sklearn.manifold.MDS : Fitted MDS model
    """
    mds = MDS(n_components=n_components, random_state=random_state, dissimilarity='euclidean')
    embedding = mds.fit_transform(features)
    return embedding, mds


def compute_tsne_embedding(features, n_components=2, perplexity=5, random_state=42):
    """
    Compute t-SNE embedding of node features.
    
    Parameters:
    -----------
    features : numpy.ndarray
        Feature matrix
    n_components : int
        Number of dimensions
    perplexity : float
        Perplexity parameter
    random_state : int
        Random seed
        
    Returns:
    --------
    numpy.ndarray : Embedded coordinates
    sklearn.manifold.TSNE : Fitted t-SNE model
    """
    tsne = TSNE(n_components=n_components, perplexity=perplexity, 
                random_state=random_state, init='pca')
    embedding = tsne.fit_transform(features)
    return embedding, tsne


def plot_embedding(embedding, labels=None, node_ids=None, title="Embedding Visualization",
                   ax=None, color_map=None, figsize=(10, 8)):
    """
    Plot 2D embedding of nodes.
    
    Parameters:
    -----------
    embedding : numpy.ndarray
        2D embedding coordinates
    labels : list or dict, optional
        Labels for coloring (community/cluster assignments)
    node_ids : list, optional
        Node IDs for annotation
    title : str
        Plot title
    ax : matplotlib.axes, optional
        Axes to plot on
    color_map : dict, optional
        Color mapping for labels
    figsize : tuple
        Figure size
        
    Returns:
    --------
    matplotlib.figure.Figure : Figure object
    matplotlib.axes.Axes : Axes object
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        fig = ax.figure
    
    # Prepare colors
    if labels is not None:
        if isinstance(labels, dict):
            unique_labels = sorted(set(labels.values()))
            if color_map is None:
                colors_list = plt.cm.Set3(np.linspace(0, 1, len(unique_labels)))
                color_map = {label: colors_list[i] for i, label in enumerate(unique_labels)}
            colors = [color_map.get(labels.get(node_id, 0), 'gray') 
                     for node_id in node_ids] if node_ids else list(labels.values())
        else:
            unique_labels = sorted(set(labels))
            if color_map is None:
                colors_list = plt.cm.Set3(np.linspace(0, 1, len(unique_labels)))
                color_map = {label: colors_list[i] for i, label in enumerate(unique_labels)}
            colors = [color_map.get(label, 'gray') for label in labels]
    else:
        colors = 'blue'
    
    # Plot points
    scatter = ax.scatter(embedding[:, 0], embedding[:, 1], c=colors, 
                        s=100, alpha=0.7, edgecolors='black', linewidths=1)
    
    # Annotate nodes
    if node_ids:
        for i, node_id in enumerate(node_ids):
            ax.annotate(node_id, (embedding[i, 0], embedding[i, 1]), 
                       fontsize=8, alpha=0.7)
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Dimension 1', fontsize=12)
    ax.set_ylabel('Dimension 2', fontsize=12)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig, ax

