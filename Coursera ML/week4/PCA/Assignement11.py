import pandas
from sklearn.decomposition import PCA
from numpy import corrcoef

data = pandas.read_csv('close_prices.csv')
del data['date']
pca = PCA(n_components=10)
pca.fit(data)
print pca.explained_variance_ratio_
print sum(pca.explained_variance_ratio_)
data = pca.transform(data)
data = data[:, 0]

dj = pandas.read_csv('djia_index.csv')
del dj['date']
dj = dj.as_matrix().tolist()
data = data.tolist()
dj_list = []
for i in range(len(dj)):
	dj_list.append(dj[i][0]) 
print len(data), len(dj)
#print dj_list
print corrcoef(data, dj_list)

# Exs 3
max_ = abs(pca.components_[0][0])
number = 0
for i in range(len(pca.components_[0])):
	print i
	if abs(pca.components_[0][i]) > max_:
		max_ = abs(pca.components_[0][i])
		number = i
data = pandas.read_csv('close_prices.csv')
del data['date']
print list(data.columns.values)[number]
print number

