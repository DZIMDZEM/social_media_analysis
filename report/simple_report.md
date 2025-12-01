# Zachary Karate Club: Network Analysis Report

## Quick Summary

Analyzed a social network of 34 karate club members to identify key individuals and understand how the club split into two factions. The analysis successfully identified the most central members and detected communities that match the actual split.

---

## Main Results

### 🔑 Most Important Members

Three members stood out as the most central:

1. **Member 33** (Mr. Hi faction leader)
   - Highest number of connections (degree centrality: 0.515)
   - Can reach everyone fastest (closeness centrality: 0.569)

2. **Member 0** (Officer faction leader)  
   - Acts as bridge between groups (betweenness centrality: 0.438)
   - Second most connected (degree: 0.485)

3. **Member 32**
   - Third most central across all measures

These three members were the key leaders whose conflict led to the club's split.

### 🎯 Community Detection Results

**Question:** Can we detect the two factions automatically?

**Answer: YES!** Both methods worked very well:

- **Louvain Algorithm:** Found 4 communities (3 pure Mr. Hi groups + 1 mostly Officer group)
  - Modularity: 0.444
  - Three communities were 100% pure Mr. Hi faction
  - One community had 92.9% Officer faction
  - Successfully identified clear faction structure

- **Girvan-Newman Algorithm:** Found 2 groups with excellent accuracy
  - Modularity: 0.348
  - One community: 100% pure Mr. Hi (15 nodes)
  - Other community: 89.5% Officer faction (19 nodes, 17 Officer, 2 Mr. Hi)

Both algorithms successfully identified the faction structure, with Girvan-Newman providing a cleaner 2-group partition that matches the actual split.

### 🧪 KMeans Clustering Results

We also tested KMeans clustering using **only centrality measures** (without the ground truth faction labels):
- **Result:** Only 50% accuracy (essentially random)
- **Finding:** Structural properties alone (centrality values) are not sufficient to predict the split
- **Comparison:** This shows that community detection algorithms (which use network connections) work much better than simple feature-based clustering

### 📊 Network Facts

- 34 members, 78 friendships
- Two clear groups visible in the network
- Highly clustered structure (57% clustering coefficient)
- Short path lengths (average: 2.4 steps between any two members)

### 💡 Key Insights

1. **Network structure predicts the split:** The way people were connected determined which faction they joined

2. **Leaders are identifiable:** The most central members (nodes 33, 0, 32) correspond to the faction leaders

3. **Automatic detection works:** Community detection algorithms successfully found groups matching the actual split
   - Girvan-Newman achieved near-perfect separation (100% and 89.5% purity)
   - Louvain found finer-grained structure with 4 highly pure communities

4. **Structural features alone are limited:** KMeans clustering using only centrality measures achieved only 50% accuracy, showing that structural properties alone aren't sufficient - community detection algorithms that consider network topology work much better

5. **Visual confirmation:** Network plots and embeddings (MDS, t-SNE, PCA) clearly show separation between the two groups

---

## What We Did

1. **Measured importance** using three centrality metrics (degree, betweenness, closeness)
2. **Detected communities** using two different algorithms (Louvain and Girvan-Newman)
3. **Clustered members** using KMeans on centrality features (without ground truth labels)
4. **Visualized results** using network plots and 2D embeddings (MDS, t-SNE, PCA)

---

## Bottom Line

The analysis successfully answered both questions:

✅ **Which members were most central?**  
   → Members 0, 32, and 33 (the faction leaders)

✅ **Do detected communities match the real split?**  
   → Yes! Girvan-Newman achieved 100% and 89.5% purity in the two groups. Louvain found 4 highly pure communities (three 100% pure, one 92.9% pure).

This shows that network analysis methods are powerful tools for understanding social structures and predicting group behavior.

---

**Analysis Date:** 2025  
**Dataset:** Zachary Karate Club (34 nodes, 78 edges)  
**Tools:** NetworkX, Python-Louvain, scikit-learn, matplotlib

---

**Note:** The analysis used only structural features (centrality measures) for clustering, without the ground truth faction labels, to test whether network properties alone could predict the split.

