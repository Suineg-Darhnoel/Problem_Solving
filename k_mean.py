import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# generate dataset
dataset = make_blobs(
            n_samples=200,
            centers=4,
            n_features=2,
            cluster_std=1.6,
            random_state=50
        )

points = dataset[0]

# import kmeans
from sklearn.cluster import KMeans

# create a kmeans objects
km = KMeans(n_clusters=4)

# fit the kmeans object to the dataset
km.fit(points)

# plot graph of generated blobs
# plt.scatter(dataset[0][:, 0], dataset[0][:, 1])
# plt.show()

clusters = km.cluster_centers_
print(clusters)

y_km = km.fit_predict(points)
# scatter every cluster centers
for center in clusters:
    x, y = center
    plt.scatter(x, y, marker='*', s=200, color='black')

plt.scatter(points[y_km == 0, 0], points[y_km == 0, 1], s=50, color='red')
plt.scatter(points[y_km == 1, 0], points[y_km == 1, 1], s=50, color='blue')
plt.scatter(points[y_km == 2, 0], points[y_km == 2, 1], s=50, color='green')
plt.scatter(points[y_km == 3, 0], points[y_km == 3, 1], s=50, color='cyan')
plt.show()
