import numpy as np
import pandas
from sklearn.tree import DecisionTreeClassifier

# data preprocessing
data = pandas.read_csv('titanic.csv', index_col='PassengerId', dtype={"Age": np.float64})
data = data.drop(['Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked'], axis=1)
data = data.dropna()
labels = data['Survived']
data = data.drop('Survived', axis=1)
print labels.head(10), '\n', data.head(10)
data['Sex'][data['Sex'] == 'male'] = 1
data['Sex'][data['Sex'] == 'female'] = 0

# fit decision tree classifier
clf = DecisionTreeClassifier(random_state=241)
clf.fit(data, labels)
importances = clf.feature_importances_
print importances
