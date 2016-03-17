import numpy as np

#EXERSICE 1
print 'EXERSICE 1'
# matrix 1000x50 of normal random variables with mean=1 and sd=10
X = np.random.normal(loc=1, scale=10, size=(1000, 50))
# mean of columns
mean = np.mean(X, axis=0)
# sd of columns
sd = np.std(X, axis=0)
X_norm = ((X - mean) / sd)
print X_norm


#EXERSICE 2
print '\nEXERSICE 2'
Z = np.array([[4, 5, 0], 
             [1, 9, 3],              
             [5, 1, 1],
             [3, 3, 3], 
             [9, 9, 9], 
             [4, 7, 1]])
print np.nonzero(np.sum(Z, axis=1) > 10)

#EXERSICE 3
print '\nEXERSICE 3'
eye1 = np.eye(3,3)
eye2 = np.eye(6,3)
EYE = np.vstack((eye1, eye2))
print EYE
