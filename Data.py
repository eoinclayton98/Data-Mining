import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits
from pandas import DataFrame

from sklearn.linear_model import LinearRegression


regression_model = LinearRegression()

dataset = pd.read_csv('dataset.csv')

Date = np.array([[2015],[2016], [2017], [2018]])

for index, row in dataset.iterrows():

	Name = row['Name']

	Revenue = np.array([row['Revenues 2015'], row['Revenues 2016'], row['Revenues 2017'], row['Revenues 2018']])
	Profits = np.array([row['Profits 2015'], row['Profits 2016'], row['Profits 2017'], row['Profits 2018']])
	Assets = np.array([row['Assets 2015'], row['Assets 2016'], row['Assets 2017'], row['Assets 2018']])
	Employees = np.array([row['Employees 2015'], row['Employees 2016'], row['Employees 2017'], row['Employees 2018']])
	MarketValue = np.array([row['Market Value 2015'], row['Market Value 2016'], row['Market Value 2017'], row['Market Value 2018']])


	regression_model.fit(Date, Revenue)
	Revenue_predict = regression_model.predict([[2019]])

	#Profits
	regression_model.fit(Date, Profits)
	Profit_predict = regression_model.predict([[2019]])

	#Assets
	regression_model.fit(Date, Assets)
	Assets_predict = regression_model.predict([[2019]])

	#Employees
	regression_model.fit(Date, Employees)
	Employees_predict = regression_model.predict([[2019]])

	#Market Value
	regression_model.fit(Date, MarketValue)
	MV_predict = regression_model.predict([[2019]])

	Rank = row['Rank']

	if row['Rank'] == 1:
		Data = pd.DataFrame({
			"Name": Name,
			"Revenue": Revenue_predict,
			"Profits": Profit_predict,
			"Assets": Assets_predict,
			"Employees": Employees_predict,
			"Market Value": MV_predict
			})
		df = DataFrame(Data, columns = ["Name", "Revenue", "Profits", "Assets", "Employees", "Market Value"])

	else:
		Data = pd.DataFrame({

			"Name": Name,
			"Revenue": Revenue_predict,
			"Profits": Profit_predict,
			"Assets": Assets_predict,
			"Employees": Employees_predict,
			"Market Value": MV_predict
			})
		df2 = df.append(DataFrame(Data, columns = ["Name", "Revenue", "Profits", "Assets", "Employees", "Market Value"]))
		df = df2



final_df = df.sort_values(by=['Revenue'], ascending=False)

j = 1
Rank = []

for index, row in dataset.iterrows():

	i = j
	Rank.append(i)

	i = i + 1
	j = i


final_df['Rank'] = Rank

cols = final_df.columns.tolist()

cols = cols[-1:] + cols[:-1]

print(final_df[cols])

final_df.to_csv('dataset_prediction.csv', encoding='utf-8', index=False)