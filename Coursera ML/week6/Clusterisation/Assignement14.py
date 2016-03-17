from sklearn.cluster import KMeans
from skimage.io import imread
from skimage import img_as_float
from pandas import DataFrame

image = imread('parrots.jpg')
image = img_as_float(image)
data = DataFrame(image[0], columns = ['R', 'G', 'B'])
print data

k_means = KMeans(init='k-means++', random_state=241)
k_means.fit(data)
values = k_means.cluster_centers_.squeeze()
print values
labels = k_means.labels_
print labels

#713x474
