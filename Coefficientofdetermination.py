from pandas import DataFrame
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score


df = pd.read_csv('r2Score.csv')

#print(df1['Name'])
#print(df2['Name'])





#print(df1['Name'])

print("Coefficient of determination:")

print(r2_score(df['Rank P'], df['Rank 2019']))


"""
df1['NameMatch?'] = np.where(df1.Name == df2.Name2, 'True', 'False')  #create new column in df1 to check if prices match
print (df1)
"""