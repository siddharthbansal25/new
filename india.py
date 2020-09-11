import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

#load data
data=pd.read_csv("india_cases_updated.csv",sep=",")
data=data[['id','cases']]
print(data.head())

#prepare data
x=np.array(data['id']).reshape(-1,1)
y=np.array(data['cases'])
plt.plot(y,'-b')


polyfeat=PolynomialFeatures(degree=3)
x=polyfeat.fit_transform(x)
#print(x)

#training data


model=linear_model.LinearRegression()
model.fit(x,y)
accuracy=model.score(x,y)
print(round(accuracy*100,3))
y0=model.predict(x)
plt.plot(y0,'--r')
plt.show()
#prediction
days=0#238 days matlab 24/08/20 ka data hai
print(round(int(model.predict(polyfeat.fit_transform([[days+179]])))/100000,2))