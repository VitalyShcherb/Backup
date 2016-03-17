from math import exp
from sklearn.metrics import roc_auc_score
import numpy as np
from numpy import zeros
import pandas

def helper(X, y, w, j):
	res = 0
	for i in range(len(y)):
		index = -y[i]*(w[0] * X.iloc[i,0] + w[1] * X.iloc[i, 1])
		res += y[i] * X.iloc[i,j] * (1 - 1 / (1 + exp(index)))	
	return res

def grad_des(X, y, alpha=0.1, C=0, eps=1e-05):
	w = [0, 0]
	temp = [0, 0]
	converged = False
	while not converged:
		temp[0] = w[0] + (alpha / len(y)) * helper(X, y, w, 0) - alpha * C * w[0] 		 
		temp[1] = w[1] + (alpha / len(y)) * helper(X, y, w, 1) - alpha * C * w[1]  
		if abs(temp[0] - w[0]) < eps and abs(temp[1] - w[1]) < eps:
			converged = True
		w[0] = temp[0]
		w[1] = temp[1]
		#print w[0] ,w[1]
	return w

def prob_calc(X ,w):
	res = zeros(len(X))
	for i in range(len(X)):
		res[i] =  1 / (1 + exp(-w[0] * X.iloc[i, 0] - w[1] * X.iloc[i, 1]))
	return res
	
data = pandas.read_csv('data-logistic.csv', header=None)
y = data.iloc[:, 0]
X = data.iloc[:, 1:]
w = grad_des(X, y, C=0)
print 'C = 0', 'w = ', w
pred = prob_calc(X, w)
print 'Roc score = ', roc_auc_score(y, pred)

w = grad_des(X, y, C=10)
print 'C = 10', 'w = ', w
pred = prob_calc(X, w)
print 'Roc score = ', roc_auc_score(y, pred)
