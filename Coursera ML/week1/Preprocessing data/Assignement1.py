import pandas
import numpy as np
import nltk
import re

data = pandas.read_csv('titanic.csv', index_col='PassengerId', dtype={"Age": np.float64})
print data.head(5)
data.info()
print("----------------------------")
data.info()

# EXERSICE 1: number of male,female
print '\n', data['Sex'].value_counts()

# EXERSICE 2: percent of survived passangers
survived = data['Survived'].value_counts()
#print '\n', survived
print '\nSurvived =', survived[1] / float(np.sum(survived)), '%'

# EXERSICE 3: percent of first class passangers
pclass = data['Pclass'].value_counts()
print pclass
print '\nFirst class =', pclass[1] / float(np.sum(pclass)), '%'

# EXERSICE 4: Mean and median age
age = data['Age']
import statistics
print '\nMeanAge =', age.mean(), 'MedianAge =', age.median()

# EXERSICE 5: brothers/sisters corelation parents/kids
print '\nCorr =', np.corrcoef(data['SibSp'], data['Parch'])


def getName(fullName):    
    # ... Mrs. xxx (Name ....    
    if fullName.find('Mrs.') > -1:         
        res = re.findall('\(([\w]*)', fullName)    
    # ... Miss. Name ...    
    else:        
        res = re.findall('\.\s([\w]*)', fullName)        
    #  in some cases name for Mrs. is after coma
    if (len(res)==0):        
        res = re.findall('\,\s([\w]*)', fullName)      
    return res[0]

# EXERSICE 6: brothers/sisters corelation parents/kids
name = data['Name']
femname = {}
for i in range(len(name)):
	if data['Sex'][i+1] == 'female': 
		#if name[i+1].find('Mrs.') != -1:
			#pos1 = name[i+1].find('(') + 1
			#pos2 = name[i+1].find(' ', pos1,)
		#else:
			#pos1 = name[i+1].find('Miss.') + 6
			#pos2 = name[i+1].find(' ', pos1,) 
		#if pos2 == -1:
			#fem = name[i+1][pos1:]
		#else:	
			#fem = name[i+1][pos1:pos2]
		#femname[fem] = femname.get(fem, 0) + 1		
		#print '\ni = ', i, 'pos = ',pos1, pos2, 'name = ',fem , 
		#print '\nfull = ', name[i+1]	
		fem = getName(name[i+1])
		femname[fem] = femname.get(fem, 0) + 1		

print '\nMost popular female name = ', max(femname, key=femname.get),\
		femname[max(femname, key=femname.get)], 'times'


