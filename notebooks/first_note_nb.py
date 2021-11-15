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

# %%
print('something')

# %%
x = np.random.randint(0,10,10)
y = np.random.randint(0,10,7)
X, Y = np.meshgrid(x, y)
print(X)
print(Y)

# %%
X, Y = np.mgrid[0:5, 1:12:2]
print(X)
print(Y)
# %%
a = np.array([3,6,9])
print(a[0])

# %%
