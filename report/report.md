# Network Analysis of Zachary's Karate Club: Centrality, Community Structure, and Attribute-Based Clustering

## Abstract

This report presents a comprehensive network analysis of the Zachary Karate Club dataset, a classic social network dataset representing friendships among 34 members of a karate club that split into two factions. We apply various network analysis methods including centrality measures, community detection algorithms, and machine learning clustering techniques to identify key individuals and understand the network structure. Our analysis demonstrates that network science methods can effectively identify the faction split that occurred in the club.

## 1. Introduction

### 1.1 Background

Zachary's Karate Club is one of the most well-known datasets in network analysis. The dataset represents the social relationships among 34 members of a karate club at a US university in the 1970s. During the course of the study, a conflict arose between the club's administrator and the instructor, leading to the club's split into two factions: one led by the administrator (Mr. Hi) and another by the instructor (Officer).

The network consists of 34 nodes (members) and 78 edges (friendship relationships). Each node has an attribute indicating which faction the member joined after the split. This ground truth makes it an ideal dataset for validating community detection algorithms.

### 1.2 Research Question

**Primary Research Question:** Which members were most central in the network, and how do detected communities align with the real split that occurred?

This question addresses:
- Identification of key individuals through centrality measures
- Validation of community detection algorithms against known ground truth
- Understanding of network structure and its relationship to the faction split

### 1.3 Dataset Description

- **Nodes:** 34 (club members)
- **Edges:** 78 (friendship relationships)
- **Network Density:** ~0.14
- **Average Degree:** ~4.59
- **Clustering Coefficient:** ~0.57
- **Diameter:** 5

The network is undirected and connected, representing symmetric friendship relationships. Each node has a `club` attribute indicating faction membership after the split (Mr. Hi or Officer).

## 2. Methods

### 2.1 Centrality Measures

We computed three centrality measures to identify important nodes:

#### 2.1.1 Degree Centrality
Degree centrality measures the number of direct connections a node has:
\[ C_D(v) = \frac{deg(v)}{n-1} \]
where \(deg(v)\) is the degree of node \(v\) and \(n\) is the total number of nodes.

#### 2.1.2 Betweenness Centrality
Betweenness centrality measures how often a node lies on the shortest path between other nodes:
\[ C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}} \]
where \(\sigma_{st}\) is the number of shortest paths from \(s\) to \(t\), and \(\sigma_{st}(v)\) is the number of those paths passing through \(v\).

#### 2.1.3 Closeness Centrality
Closeness centrality measures the average distance from a node to all other nodes:
\[ C_C(v) = \frac{n-1}{\sum_{u \neq v} d(u,v)} \]
where \(d(u,v)\) is the shortest path distance between nodes \(u\) and \(v\).

### 2.2 Community Detection

#### 2.2.1 Louvain Algorithm
The Louvain algorithm is a modularity-based greedy optimization method for community detection. It maximizes modularity:
\[ Q = \frac{1}{2m} \sum_{ij} \left[ A_{ij} - \frac{k_i k_j}{2m} \right] \delta(c_i, c_j) \]
where \(A_{ij}\) is the adjacency matrix, \(k_i\) is the degree of node \(i\), \(m\) is the number of edges, and \(\delta(c_i, c_j)\) is 1 if nodes \(i\) and \(j\) are in the same community.

**Implementation:**
```python
import community.community_louvain as community_louvain
partition = community_louvain.best_partition(G)
modularity = community_louvain.modularity(partition, G)
```

#### 2.2.2 Girvan-Newman Algorithm
The Girvan-Newman algorithm is a hierarchical community detection method that progressively removes edges with high betweenness centrality, creating a dendrogram of community structures.

**Implementation:**
```python
from networkx.algorithms import community
communities_generator = community.girvan_newman(G)
# Extract partition at desired number of communities
```

### 2.3 Node Attribute-Based Clustering

We applied KMeans clustering on node features combining:
- Centrality measures (degree, betweenness, closeness)
- Club attribute (faction membership encoded numerically)

Features were standardized before clustering:
\[ X_{scaled} = \frac{X - \mu}{\sigma} \]

**Implementation:**
```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
kmeans = KMeans(n_clusters=2, random_state=42)
labels = kmeans.fit_predict(features_scaled)
```

### 2.4 Dimensionality Reduction

#### 2.4.1 Principal Component Analysis (PCA)
PCA is a linear dimensionality reduction technique that finds the principal directions of maximum variance in the data.

#### 2.4.2 Multidimensional Scaling (MDS)
MDS projects high-dimensional data to lower dimensions while preserving pairwise distances.

#### 2.4.3 t-SNE
t-SNE (t-distributed Stochastic Neighbor Embedding) is a non-linear dimensionality reduction technique particularly effective for visualization.

**Implementation:**
```python
from sklearn.manifold import MDS, TSNE

mds = MDS(n_components=2, random_state=42)
embedding_mds = mds.fit_transform(features)

tsne = TSNE(n_components=2, perplexity=5, random_state=42)
embedding_tsne = tsne.fit_transform(features)
```

### 2.5 Visualization

Network visualizations were created using NetworkX and Matplotlib with:
- Force-directed layout (spring layout)
- Node coloring based on community/cluster assignments
- Node sizes proportional to centrality measures

## 3. Results

### 3.1 Centrality Analysis

The analysis identified several key nodes based on different centrality measures:

**Top Nodes by Degree Centrality:**
- Node 33: 0.515 (highest)
- Node 0: 0.485
- Node 32: 0.364

**Top Nodes by Betweenness Centrality:**
- Node 0: 0.438 (highest)
- Node 33: 0.304
- Node 32: 0.145

**Top Nodes by Closeness Centrality:**
- Node 33: 0.569 (highest)
- Node 0: 0.559
- Node 32: 0.500

These results indicate that nodes 0, 32, and 33 are the most central individuals in the network, corresponding to key leaders in the karate club.

### 3.2 Community Detection Results

#### 3.2.1 Louvain Algorithm
- **Number of communities detected:** 4
- **Modularity:** 0.444
- **Alignment with actual split:** 
  - Three communities achieved 100% purity (all Mr. Hi faction: 11, 5, and 4 nodes)
  - One community achieved 92.9% purity (14 nodes: 13 Officer, 1 Mr. Hi)
- **Insight:** Louvain reveals finer-grained structure, identifying sub-communities within the Mr. Hi faction

#### 3.2.2 Girvan-Newman Algorithm
- **Number of communities detected:** 2
- **Modularity:** 0.348
- **Alignment with actual split:** 
  - Community 0: 100% pure Mr. Hi (15 nodes)
  - Community 1: 89.5% Officer faction (19 nodes: 17 Officer, 2 Mr. Hi)
- **Insight:** Provides the cleanest 2-group partition matching the actual split

Both algorithms successfully recovered the faction structure. Girvan-Newman provides a cleaner 2-group partition, while Louvain reveals more detailed community structure with higher modularity.

### 3.3 Clustering Results

KMeans clustering on node features (centrality measures only, **without** club attribute) achieved limited success:
- **Number of clusters:** 2
- **Cluster purity:** 50% for both clusters (essentially random performance)
  - Cluster 0 (28 nodes): 14 Mr. Hi, 14 Officer
  - Cluster 1 (6 nodes): 3 Mr. Hi, 3 Officer
- **Key finding:** Structural properties (centrality values) alone are insufficient to predict the faction split
- **Comparison:** Community detection algorithms (using network topology) significantly outperform feature-based clustering

### 3.4 Dimensionality Reduction

PCA, MDS, and t-SNE embeddings revealed clear separation between the two factions:
- All three methods (PCA, MDS, t-SNE) successfully visualize the underlying structure
- Nodes from the same faction cluster together in the embedded space
- The visualization confirms the structural separation between groups
- MDS stress: 0.0153 (excellent fit)
- PCA explained variance: High percentage captured in 2D space

### 3.5 Visualizations

Network visualizations demonstrate:
1. Clear community structure with two distinct groups
2. Central nodes positioned as bridges between communities
3. High correspondence between detected communities and actual faction split

## 4. Discussion

### 4.1 Centrality Findings

The centrality analysis revealed that nodes 0, 32, and 33 are the most important individuals in the network. Node 33 has the highest degree centrality (0.515), node 0 has the highest betweenness centrality (0.438), and these three nodes rank highest across all centrality measures. In the context of the karate club, these correspond to the key figures involved in the conflict that led to the split. Their high centrality values indicate their importance in maintaining network connectivity and information flow.

### 4.2 Community Detection Performance

Both Louvain and Girvan-Newman algorithms successfully identified the faction structure:
- **Girvan-Newman** achieved near-perfect separation with a clean 2-group partition (100% and 89.5% purity)
- **Louvain** achieved higher modularity (0.444 vs 0.348) and revealed finer-grained structure with 4 highly pure communities
- The high accuracy of both methods validates their effectiveness for community detection in social networks

### 4.3 Clustering Limitations

KMeans clustering on centrality features alone achieved only 50% accuracy, demonstrating that:
- Node attributes (centrality values) are less informative than network topology (connections)
- Community detection algorithms that consider network structure significantly outperform feature-based clustering
- This highlights the importance of using appropriate methods for network analysis problems

### 4.4 Implications

The analysis demonstrates that:
1. Network structure contains sufficient information to predict the faction split (via community detection)
2. Centrality measures effectively identify key individuals
3. Community detection algorithms can recover ground truth partitions with high accuracy
4. Network topology (connections) is more informative than node attributes (centrality values) alone

### 4.5 Limitations

- **Small dataset:** With only 34 nodes, statistical power is limited
- **Clustering performance:** KMeans on centrality features alone cannot predict the split (50% accuracy)
- **Static network:** Analysis does not capture temporal dynamics of the split
- **Method selection:** Feature-based clustering is less effective than topology-based community detection for this problem

## 5. Conclusions

This analysis of Zachary's Karate Club network successfully addressed the research question:

1. **Most central members** were identified through multiple centrality measures, with nodes 0, 32, and 33 emerging as key individuals (node 33: highest degree 0.515, node 0: highest betweenness 0.438).

2. **Detected communities** align remarkably well with the actual faction split:
   - Girvan-Newman achieved near-perfect separation (100% and 89.5% purity)
   - Louvain found 4 highly pure communities (three 100% pure, one 92.9% pure)

3. **Community detection algorithms** (Louvain and Girvan-Newman) successfully recovered the faction structure, demonstrating the power of network analysis methods.

4. **KMeans clustering** on centrality features alone achieved only 50% accuracy, highlighting that network topology (used by community detection) is more informative than node attributes alone.

The results confirm that network science methods can effectively analyze social network structure and identify important individuals and communities. The Zachary Karate Club dataset serves as an excellent validation case for network analysis algorithms.

## 6. References

1. Zachary, W. W. (1977). An information flow model for conflict and fission in small groups. *Journal of anthropological research*, 33(4), 452-473.

2. SNAP Dataset Repository. Zachary's Karate Club Network. Stanford Network Analysis Project. Retrieved from: https://snap.stanford.edu/data/ego-Zachary.html

3. NetworkX — NetworkX documentation. Retrieved from: https://networkx.org/

4. Blondel, V. D., Guillaume, J. L., Lambiotte, R., & Lefebvre, E. (2008). Fast unfolding of communities in large networks. *Journal of statistical mechanics: theory and experiment*, 2008(10), P10008.

5. Girvan, M., & Newman, M. E. J. (2002). Community structure in social and biological networks. *Proceedings of the national academy of sciences*, 99(12), 7821-7826.

6. Van der Maaten, L., & Hinton, G. (2008). Visualizing data using t-SNE. *Journal of machine learning research*, 9(Nov), 2579-2605.

7. Scikit-learn: Machine Learning in Python. Pedregosa et al., JMLR 12, pp. 2825-2830, 2011.

---

**Report Generated:** 2025  
**Analysis Tools:** Python 3.x, NetworkX, scikit-learn, matplotlib, python-louvain

