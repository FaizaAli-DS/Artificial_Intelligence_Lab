import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import adjusted_rand_score
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

iris = load_iris()
X = StandardScaler().fit_transform(iris.data)     # scale features

# Elbow method: inertia for k = 1..8
inertias = [KMeans(n_clusters=k, n_init=10, random_state=0).fit(X).inertia_
            for k in range(1, 9)]
print("Inertia for k=1..8:", [round(i, 1) for i in inertias])

km = KMeans(n_clusters=3, n_init=10, random_state=0)
clusters = km.fit_predict(X)
print("Cluster sizes      :", np.bincount(clusters))
print("Adjusted Rand Index:", round(adjusted_rand_score(iris.target, clusters), 3))

fig, ax = plt.subplots(1, 2, figsize=(9, 3.3))
NAVY = '#0E367B'                       # Iqra University blue
ax[0].plot(range(1, 9), inertias, 'o-', color=NAVY); ax[0].set_title('Elbow method')
ax[0].set_xlabel('k'); ax[0].set_ylabel('Inertia')
for k, m in zip(range(3), ['o', 's', '^']):        # one marker shape per cluster
    pts = X[clusters == k]
    ax[1].scatter(pts[:, 2], pts[:, 3], marker=m, s=18, facecolors='none',
                  edgecolors=NAVY, label=f'Cluster {k}')
ax[1].scatter(km.cluster_centers_[:, 2], km.cluster_centers_[:, 3],
              c=NAVY, marker='X', s=140, label='Centroid')
ax[1].legend(fontsize=7)
ax[1].set_title('K-Means clusters (petal features)')
ax[1].set_xlabel('petal length (scaled)'); ax[1].set_ylabel('petal width (scaled)')
plt.tight_layout(); plt.savefig('lab10_kmeans.png', dpi=130)
