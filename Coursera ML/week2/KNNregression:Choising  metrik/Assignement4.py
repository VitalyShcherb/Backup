from sklearn.datasets import load_boston
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import scale
from sklearn.cross_validation import KFold, cross_val_score
import numpy as np
import pandas

boston = load_boston()
data = pandas.DataFrame(boston.data)
target = pandas.DataFrame(boston.target)
scale(data, copy=False)

# fit KNN regression
minkowski_p = np.linspace(1, 10, num=200)
kf = KFold(len(target), n_folds=5, random_state=42)
result = []
for i in minkowski_p:
	KNN = KNeighborsRegressor(n_neighbors=5, weights='distance',  p=i)
	cv_score = cross_val_score(KNN, data, target, cv=kf, n_jobs=-1, scoring='mean_squared_error')
	result.append((i, np.mean(cv_score)))

p, error = result[1][0], result[1][1]
for pair in result:
	if pair[1] > error:
		p, error = pair[0], pair[1]
	print pair[0], pair[1]
print 'best:', p, error	
