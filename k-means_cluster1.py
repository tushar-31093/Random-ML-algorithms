from sklearn.datasets import load_iris
from pandas.tools.plotting import parallel_coordinates
	
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4)

#df = pd.read_csv('E:/DAT210x-master/DAT210x-master/Module3/Datasets/students.data')
#df = pd.DataFrame(data.data, columns=data.feature_names) 
#df = pd.DataFrame()

ordered_satisfaction = ['Very Unhappy', 'Unhappy', 'Neutral', 'Happy', 'Very Happy']
df = pd.DataFrame({'satisfaction':['Mad', 'Happy', 'Unhappy', 'Neutral']})
df.satisfaction = df.satisfaction.astype("category",
  ordered=True,
  categories=ordered_satisfaction
).cat.codes
print(df)

kmeans.fit(df)
KMeans(copy_x=True, init='k-means++', max_iter=300, n_clusters=5, n_init=10,
	n_jobs=1, precompute_distances='auto', random_state=None, tol=0.0001,
	verbose=0)

labels = kmeans.predict(df)
centroids = kmeans.cluster_centers_
print(labels)
print(centroids)

