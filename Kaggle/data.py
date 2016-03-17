import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data into DataFrames
train_users = pd.read_csv('train_users_2.csv')
test_users = pd.read_csv('test_users.csv')

print 'Number of observations = ', train_users.shape[0], 'in the training set,',\
 		test_users.shape[0], 'in the test set.'
print 'Total users =', train_users.shape[0] + test_users.shape[0]

# Merge train and test users
users = pd.concat((train_users, test_users), axis=0, ignore_index=True)

# Remove ID's since now we are not interested in making predictions
users.drop('id', axis=1, inplace=True)

# Missing values
col_names = ['first_browser', 'first_device_type', 'gender', 'language']  
values = [users[name].value_counts() for name in col_names]
for i in values: 
	print '/n'
	print i
# replacing 'unknow' to NA
users.gender.replace('-unknown-', np.nan, inplace=True)

# how much data we are missing
users_nan = (users.isnull().sum() / users.shape[0]) * 100
print '\n', users_nan[users_nan > 0].drop('country_destination')


print "Just for the sake of curiosity; we have", \
	int((train_users.date_first_booking.isnull().sum() / float(train_users.shape[0])) * 100), \
	"% of missing values at date_first_booking in the training data"

