from pandas import DataFrame
import pandas as pd
import numpy as np


df1 = pd.read_csv('revenue.csv')

#print(df1['Name'])
#print(df2['Name'])


count = 0
true1 = 0

true2 = 0

for index, row in df1.iterrows():
	count = count + 1


	if row['R2019'] == row['RP']:
		true1 = true1 + 1

"""
	for index2, row2 in df1.iterrows():
		if row['Name'] == row2['Name2'] and row2['Rank2'] > row['Rank'] - 5 and row2['Rank2'] < row['Rank'] + 5:
			true2 = true2 + 1
			break
"""



score1 = true1 / float(count)

#score2 = true2 / float(count)

print("Perfectly Matched:")

print(score1)

#print("Within 10:")
#print(score2)

"""
df1['NameMatch?'] = np.where(df1.Name == df2.Name2, 'True', 'False')  #create new column in df1 to check if prices match
print (df1)
"""