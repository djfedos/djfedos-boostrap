#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
%matplotlib inline

mu = 70
sigma = 6.6

sample = sigma * np.random.randn(1000) + mu
plt.hist(sample)
plt.show()