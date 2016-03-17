import pandas
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import KFold
from numpy import zeros	
import numpy
from numpy import array
from sklearn.metrics import r2_score
	
data = pandas.read_csv('abalone.csv')
data['Sex'] = data['Sex'].map(lambda x: 1 if x == 'M' else (-1 if x == 'F' else 0))
labels = data['Rings']
del data['Rings']

result = zeros(51)
for i in xrange(1,51):
	kf = KFold(len(labels), n_folds=5, random_state=1, shuffle=True)
	for train_index, test_index in kf:
		X_train, X_test = array(data.loc[train_index,:]), array(data.loc[test_index,:])
		y_train, y_test = array(labels[train_index]), array(labels[test_index])
		RF = RandomForestRegressor(n_estimators=i, n_jobs=-1, random_state=1)
		RF.fit(X_train, y_train)
		result[i] += r2_score(y_test, RF.predict(X_test))
	result[i] = result[i] / 5.0
for i in range(len(result)):
	print i, result[i]

