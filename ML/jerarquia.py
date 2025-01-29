# Utilizaremos el agrupamiento aglomerativo, un tipo de agrupamiento jerárquico que sigue un enfoque ascendente.
# Comenzamos tratando cada punto de datos como su propio grupo.
# Luego, unimos los grupos que tienen la distancia más corta entre ellos para crear grupos más grandes.
# Este paso se repite hasta que se forma un grupo grande que contiene todos los puntos de datos.

# La agrupación jerárquica requiere que decidamos tanto el método de distancia como el de vinculación.
# Utilizaremos la distancia euclidiana y el método de vinculación de Ward, 
# que intenta minimizar la varianza entre los grupos

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# plt.scatter(x, y)
# plt.show()

# Ahora calculamos el vínculo de ward utilizando la distancia euclidiana y
# lo visualizamos utilizando un dendrograma:

# data = list(zip(x, y))

# linkage_data = linkage(data, method='ward', metric='euclidean')
# dendrogram(linkage_data)

# plt.show()

data = list(zip(x, y))

hierarchical_cluster = AgglomerativeClustering(n_clusters=2, linkage='ward')
labels = hierarchical_cluster.fit_predict(data)

plt.scatter(x, y, c=labels)
plt.show()