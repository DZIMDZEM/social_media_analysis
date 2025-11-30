# Network Analysis of Zachary's Karate Club

## 📊 Project Overview

This repository contains a complete network analysis project focusing on Zachary's Karate Club dataset. The project explores centrality measures, community detection algorithms, and attribute-based clustering to understand the social network structure and identify key individuals.

**Research Question:** Which members were most central in the network, and how do detected communities align with the real split that occurred?

## 🗂 Repository Structure

```
/
├── data/
│   ├── karate.edgelist       # Network edge list format
│   └── metadata.json         # Dataset description and metadata
│
├── src/
│   ├── load_data.py          # Data loading utilities
│   ├── centrality.py         # Centrality measure computations
│   ├── communities.py        # Community detection algorithms
│   ├── clustering.py         # Node attribute-based clustering
│   ├── visualization.py      # Network visualization functions
│   └── utils.py              # Helper utility functions
│
├── notebooks/
│   └── project_analysis.ipynb # Full analysis notebook
│
├── report/
│   ├── report.md             # Markdown version of the report
│   └── report.pdf            # PDF version (to be generated)
│
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore rules
```

## 🚀 Quick Start

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd social_media_analysis
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Analysis

#### Option 1: Jupyter Notebook (Recommended)

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Navigate to `notebooks/project_analysis.ipynb` and run all cells.

#### Option 2: Python Scripts

You can also use the modules directly in Python:

```python
from src.load_data import load_graph
from src.centrality import compute_all_centralities
from src.communities import louvain_communities

# Load data
G, metadata = load_graph(source='networkx')

# Compute centralities
centralities_df = compute_all_centralities(G)

# Detect communities
partition, modularity = louvain_communities(G)
```

## 📖 Dataset

The Zachary Karate Club dataset represents friendships among 34 members of a karate club at a US university in the 1970s. The club split into two factions:
- **Mr. Hi faction** (instructor's group)
- **Officer faction** (administrator's group)

**Network Properties:**
- Nodes: 34
- Edges: 78
- Network Density: ~0.14
- Average Clustering Coefficient: ~0.57

The dataset is loaded from NetworkX's built-in graph library, and the edge list is automatically generated in `data/karate.edgelist`.

**Reference:** Zachary, W. W. (1977). An information flow model for conflict and fission in small groups. *Journal of anthropological research*, 33(4), 452-473.

**SNAP Dataset:** https://snap.stanford.edu/data/ego-Zachary.html

## 🔍 Methods Implemented

### Centrality Measures
- **Degree Centrality**: Number of direct connections
- **Betweenness Centrality**: Frequency of being on shortest paths
- **Closeness Centrality**: Average distance to all other nodes

### Community Detection
- **Louvain Algorithm**: Modularity-based greedy optimization
- **Girvan-Newman Algorithm**: Hierarchical edge removal method

### Clustering
- **KMeans Clustering**: On node features (centralities + attributes)
- **Hierarchical Clustering**: Agglomerative clustering option

### Dimensionality Reduction
- **MDS**: Multidimensional Scaling
- **t-SNE**: t-distributed Stochastic Neighbor Embedding
- **UMAP**: Uniform Manifold Approximation and Projection (optional)

### Visualization
- Network graphs with force-directed layouts
- Community-colored visualizations
- Centrality-based node sizing
- 2D embeddings (MDS/t-SNE)

## 📊 Key Results

1. **Most Central Nodes**: Nodes 0, 32, and 33 identified as key individuals
2. **Community Detection**: Both Louvain and Girvan-Newman successfully identified the two factions
3. **Alignment**: Detected communities align well with the actual split (high accuracy)
4. **Visualization**: Clear separation between factions in embedding spaces

## 📝 Report

A comprehensive markdown report is available in `report/report.md`. It includes:
- Introduction and background
- Methods description with code snippets
- Results and findings
- Discussion and conclusions
- References

To generate a PDF version:
```bash
# Using pandoc (if installed)
pandoc report/report.md -o report/report.pdf
```

## 🛠 Dependencies

- **networkx**: Network analysis and graph manipulation
- **python-louvain**: Louvain community detection algorithm
- **scikit-learn**: Machine learning and clustering
- **pandas**: Data manipulation and analysis
- **matplotlib**: Plotting and visualization
- **seaborn**: Statistical visualization
- **umap-learn**: UMAP dimensionality reduction (optional)
- **jupyter**: Interactive notebook environment

See `requirements.txt` for specific versions.

## 🧪 Usage Examples

### Compute Centrality Measures

```python
from src.centrality import compute_all_centralities, get_top_central_nodes

centralities_df = compute_all_centralities(G)
top_nodes = get_top_central_nodes(degree_dict, n=5)
```

### Detect Communities

```python
from src.communities import louvain_communities, girvan_newman_communities

# Louvain
partition, modularity = louvain_communities(G)

# Girvan-Newman
partition_gn = girvan_newman_communities(G, num_communities=2)
```

### Visualize Network

```python
from src.visualization import plot_network, plot_by_communities

# Basic network plot
fig, ax, pos = plot_network(G, title="Network Graph")

# Colored by communities
fig, ax, pos = plot_by_communities(G, partition, title="Communities")
```

### Clustering

```python
from src.clustering import prepare_node_features, kmeans_clustering

features, node_list = prepare_node_features(G, centralities_df, attributes=club_numeric)
labels, model = kmeans_clustering(features, n_clusters=2)
```

## 📚 References

1. Zachary, W. W. (1977). An information flow model for conflict and fission in small groups. *Journal of anthropological research*, 33(4), 452-473.

2. SNAP Dataset Repository: https://snap.stanford.edu/data/ego-Zachary.html

3. NetworkX Documentation: https://networkx.org/

4. Blondel, V. D., et al. (2008). Fast unfolding of communities in large networks. *Journal of statistical mechanics: theory and experiment*, 2008(10), P10008.

5. Girvan, M., & Newman, M. E. J. (2002). Community structure in social and biological networks. *Proceedings of the national academy of sciences*, 99(12), 7821-7826.

## 🤝 Contributing

This is an educational/research project. Suggestions and improvements are welcome!

## 📄 License

This project is provided for educational purposes.

## 👤 Author

Network Analysis Project - Zachary Karate Club Analysis

---

**Note:** Ensure all dependencies are installed before running the analysis. The dataset is automatically generated from NetworkX, so no manual download is required.

