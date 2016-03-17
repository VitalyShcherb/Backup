import pandas
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import KFold, cross_val_score
from sklearn.preprocessing import scale

# preparing data
data = pandas.read_csv('wine.csv', header=None)
data = data.dropna()
labels = data.loc[:,0]
data = data.loc[:,1:]

# function for fit KNN
def fit(X,Y):
	kf = KFold(len(Y), n_folds=5, random_state=42)
	result = []
	for i in range(1,51):
		KNN = KNeighborsClassifier(n_neighbors=i)
		cv_score = cross_val_score(KNN, X, Y, cv=kf, n_jobs=-1)
		result.append((i, np.mean(cv_score)))
	return result
		
# fit KNN model with CV
for pair in fit(data, labels):
	print pair[0], pair[1]

# Normalize features and fit again
print '-----------Normalazed features------------'
scale(data, copy=False)
for pair in fit(data, labels):
	print pair[0], pair[1]
