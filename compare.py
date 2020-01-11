from pandas import DataFrame
import pandas as pd
import numpy as np

df1 = pd.read_csv('dataset_prediction.csv')

df2 = pd.read_csv('2019.csv')

#print(df1['Name'])
#print(df2['Name'])


df1['Name2'] = df2['Name'] #add the Price2 column from df2 to df1
df1['Rank2'] = df2['Rank']


count = 0
true1 = 0

true2 = 0

for index, row in df1.iterrows():
	count = count + 1

	if row['Name'] == row['Name2']:
		true1 = true1 + 1


	for index2, row2 in df1.iterrows():
		if row['Name'] == row2['Name2'] and row2['Rank2'] > row['Rank'] - 5 and row2['Rank2'] < row['Rank'] + 5:
			true2 = true2 + 1
			break


score1 = true1 / float(count)

score2 = true2 / float(count)

print("Perfectly Matched:")

print(score1)

print("Within 10:")
print(score2)

"""
df1['NameMatch?'] = np.where(df1.Name == df2.Name2, 'True', 'False')  #create new column in df1 to check if prices match
print (df1)
"""