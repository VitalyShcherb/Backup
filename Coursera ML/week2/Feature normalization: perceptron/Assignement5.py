import numpy as np
import pandas
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler

# prepare data
train = pandas.read_csv('perceptron-train.csv', header=None)
test = pandas.read_csv('perceptron-test.csv', header=None)
train_labels = train.loc[:,0]
train = train.loc[:,1:]
test_labels = test.loc[:,0]
test = test.loc[:,1:]

# perceptron fitting
clf = Perceptron(random_state=241)
clf.fit(train, train_labels)
predictions = clf.predict(test)
error_1 = clf.score(test, test_labels)
print error_1

# prepare and normalizing data
train = pandas.read_csv('perceptron-train.csv', header=None)
test = pandas.read_csv('perceptron-test.csv', header=None)
train_labels = train.loc[:,0]
train = train.loc[:,1:]
test_labels = test.loc[:,0]
test = test.loc[:,1:]

scaler = StandardScaler()
train = scaler.fit_transform(train)
test = scaler.transform(test)

# perceptron fitting
clf = Perceptron(random_state=241)
clf.fit(train, train_labels)
predictions = clf.predict(test)
error_2 = clf.score(test, test_labels)
print error_2



print 'delta = ', error_2 - error_1
