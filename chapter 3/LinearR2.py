#Example 3.15a Linear Regression
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

x = [0,1,2,3,4]
y = [3,5,5,6,7]
x1=sm.add_constant(x)

model = sm.OLS(y,x1)
results = model.fit()
print (results.params)
print (results.summary())

y_pred=results.predict(x1)
plt.scatter(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x,y_pred, "r")
plt.show()
