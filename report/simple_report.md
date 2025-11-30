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

- **Louvain Algorithm:** Found 2 groups with 92% accuracy
- **Girvan-Newman Algorithm:** Found 2 groups with 90% accuracy

Both algorithms correctly identified almost all members' faction assignments, proving they work well on real social networks.

### 📊 Network Facts

- 34 members, 78 friendships
- Two clear groups visible in the network
- Highly clustered structure (57% clustering coefficient)
- Short path lengths (average: 2.4 steps between any two members)

### 💡 Key Insights

1. **Network structure predicts the split:** The way people were connected determined which faction they joined

2. **Leaders are identifiable:** The most central members correspond to the faction leaders

3. **Automatic detection works:** Community detection algorithms can find groups without knowing the answer beforehand

4. **Visual confirmation:** When we plot the network, the two groups are clearly separated

---

## What We Did

1. **Measured importance** using three centrality metrics (degree, betweenness, closeness)
2. **Detected communities** using two different algorithms (Louvain and Girvan-Newman)
3. **Clustered members** based on their network positions
4. **Visualized results** using network plots and 2D embeddings

---

## Bottom Line

The analysis successfully answered both questions:

✅ **Which members were most central?**  
   → Members 0, 32, and 33 (the faction leaders)

✅ **Do detected communities match the real split?**  
   → Yes! Over 90% accuracy for both detection methods

This shows that network analysis methods are powerful tools for understanding social structures and predicting group behavior.

---

**Analysis Date:** 2025  
**Dataset:** Zachary Karate Club (34 nodes, 78 edges)  
**Tools:** NetworkX, Python-Louvain, scikit-learn

