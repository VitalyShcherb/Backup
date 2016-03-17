from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.cross_validation import KFold, cross_val_score
import numpy as np

newsgroups = datasets.fetch_20newsgroups(
                    subset='all', 
                    categories=['alt.atheism', 'sci.space']
             )
             
TfIdf = TfidfVectorizer()
data = TfIdf.fit_transform(newsgroups.data)
labels = newsgroups.target

kf = KFold(len(labels), n_folds=5, random_state=241)

C = [10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 10**0, 10**1, 10**2, 10**3, 10**4, 10**5]
result = []
for i in C:
	SVM = SVC(C = i, kernel='linear')
	cv_score = cross_val_score(SVM, data, labels, cv=kf, n_jobs=-1)
	result.append((i, np.mean(cv_score)))

p, error = result[1][0], result[1][1]
for pair in result:
	if pair[1] > error:	
		p, error = pair[0], pair[1]
	#print pair[0], pair[1]
#print 'best:', p, error	

SVM = SVC(C = p, kernel='linear')
SVM.fit(data, labels)

all_weights = {}
positive_data = []
for i in range(len(SVM.coef_.data)):
	all_weights[abs(SVM.coef_.data[i])] =  SVM.coef_.indices[i]
	positive_data.append(abs(SVM.coef_.data[i]))
		
top10 = sorted(positive_data, reverse=True)[:10]
TOP10 = []
for i in top10:
	TOP10.append(all_weights[i])

for i in TOP10:
	print TfIdf.get_feature_names()[i]

