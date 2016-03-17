import pandas
from sklearn.metrics import accuracy_score, precision_score,\
							recall_score, f1_score, roc_auc_score,\
							precision_recall_curve

# Exercise 1
data = pandas.read_csv('classification.csv')
TP = 0
TN = 0
FN = 0
FP = 0
for i in range(len(data)):
	if data['true'][i] == 1 and data['pred'][i] == 1: 
		TP += 1
	if data['true'][i] == 0 and data['pred'][i] == 0: 
		TN += 1	
	if data['true'][i] == 1 and data['pred'][i] == 0: 
		FN += 1
	if data['true'][i] == 0 and data['pred'][i] == 1: 
		FP += 1			
print 'TP = ', TP
print 'TN = ', TN
print 'FN = ', FN
print 'FP = ', FP
print 'sum = ', TP + TN + FN + FP
print 'Accuracy = ', accuracy_score(data['true'], data['pred'])
print 'Precision = ', precision_score(data['true'], data['pred'])
print 'Recall = ', recall_score(data['true'], data['pred'])
print 'F1 = ', f1_score(data['true'], data['pred'])

# Exercise 2
data = pandas.read_csv('scores.csv')
print '\nROC Logreg = ', roc_auc_score(data['true'], data['score_logreg'])
print 'ROC SVM = ', roc_auc_score(data['true'], data['score_svm'])
print 'ROC KNN = ', roc_auc_score(data['true'], data['score_knn'])
print 'ROC Tree = ', roc_auc_score(data['true'], data['score_tree'])

precision, recall, thresholds = precision_recall_curve(data['true'], data['score_logreg'])
logreg_precision = 0
for i in range(len(precision)):
	if recall[i] >= 0.7 and precision[i] > logreg_precision:
		logreg_precision = precision[i]
print 'Highest Logreg presicion = ', logreg_precision

precision, recall, thresholds = precision_recall_curve(data['true'], data['score_svm'])
svm_precision = 0
for i in range(len(precision)):
	if recall[i] >= 0.7 and precision[i] > svm_precision:
		svm_precision = precision[i]
print 'Highest SVM presicion = ', svm_precision

precision, recall, thresholds = precision_recall_curve(data['true'], data['score_knn'])
knn_precision = 0
for i in range(len(precision)):
	if recall[i] >= 0.7 and precision[i] > knn_precision:
		knn_precision = precision[i]
print 'Highest KNN presicion = ', knn_precision

precision, recall, thresholds = precision_recall_curve(data['true'], data['score_tree'])
tree_precision = 0
for i in range(len(precision)):
	if recall[i] >= 0.7 and precision[i] > tree_precision:
		tree_precision = precision[i]
print 'Highest Tree presicion = ', tree_precision
