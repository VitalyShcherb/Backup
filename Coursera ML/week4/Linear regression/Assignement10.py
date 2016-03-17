from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Ridge
from sklearn.feature_extraction import DictVectorizer
from scipy.sparse import hstack
import pandas
import re
	
data_train = pandas.read_csv('salary-train.csv')																																						
data_test = pandas.read_csv('salary-test-mini.csv')
for i in range(len(data_train['FullDescription'])):
	text = data_train['FullDescription'][i]
	data_train['FullDescription'][i] = re.sub('[^a-zA-Z0-9]', ' ', text.lower())

for i in range(len(data_test['FullDescription'])):
	text = data_test['FullDescription'][i]
	data_test['FullDescription'][i] = re.sub('[^a-zA-Z0-9]', ' ', text.lower())

vectorizer = TfidfVectorizer(min_df=5)	
TfIdf = vectorizer.fit_transform(data_train['FullDescription'])
data_train['LocationNormalized'].fillna('nan', inplace=True)
data_train['ContractTime'].fillna('nan', inplace=True)
labels_train = data_train['SalaryNormalized']

enc = DictVectorizer()
X_train_categ = enc.fit_transform(data_train[['LocationNormalized', 'ContractTime']].to_dict('records'))
data_train = hstack([TfIdf, X_train_categ])

TfIdf = vectorizer.transform(data_test['FullDescription'])
data_test['LocationNormalized'].fillna('nan', inplace=True)
data_test['ContractTime'].fillna('nan', inplace=True)
X_test_categ = enc.transform(data_test[['LocationNormalized', 'ContractTime']].to_dict('records'))
data_test = hstack([TfIdf, X_test_categ])

# training and predicting
regression = Ridge(alpha=1)
regression.fit(data_train, labels_train)
print regression.predict(data_test)


