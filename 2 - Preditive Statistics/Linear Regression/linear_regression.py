#%%
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
#%%
array_of_scores = [3,3,5,6,5,4,2,1,4,7]
array_hours_studied = [1,1,3,4,3,2,1,0,2,5]
#%%
model = LinearRegression()
model.fit(np.array(array_hours_studied).reshape(-1,1), array_of_scores)
#%%
model.score(np.array(array_hours_studied).reshape(-1,1), array_of_scores)
# %% Ploting the linear regression

plt.scatter(array_hours_studied, array_of_scores)
plt.plot(array_hours_studied, model.predict(np.array(array_hours_studied).reshape(-1,1)), color='red')
# %%
