

import numpy as np
import pandas as  pd
import seaborn as sns
import matplotlib.pyplot as plt

tip_data = pd.read_excel('/content/tip-amount.xlsx')
tip_data.head()#display first 5 rowsq

tip_data.drop('Meal', axis=1, inplace=True)

tip_data.head()

tip_data.corr()

#target splitting

y=tip_data['Observed tip amount(yi)']
x=tip_data.drop('Observed tip amount(yi)', axis=1)

#TRAIN TEST SPLIT
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

x_test

#cresting linear regression model
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
model=lr.fit(x_train, y_train)

y_pred=model.predict(x_test)

print(y_pred)
print(y_test)

from sklearn.metrics import mean_squared_error, r2_score

print(mean_squared_error(y_test, y_pred))
print(r2_score(y_test, y_pred))

tip_data.head()

#making prediction for 50$ bill amoutnt
bill_prediction=model.predict([[100]])
print(bill_prediction)
