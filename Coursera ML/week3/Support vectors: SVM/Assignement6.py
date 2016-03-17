import pandas
from sklearn.svm import SVC

data = pandas.read_csv('svm-data.csv', header=None)
labels = data.loc[:,0]
train = data.loc[:,1:]

SVM = SVC(random_state=241, C = 100000)
SVM.fit(train, labels)
print SVM.support_

