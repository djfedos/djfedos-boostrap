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
# operations on arrays
a = np.array([3,6,9])
print(a[0])
b = a + 2
print(b)
print(a + b)
c = a * 3
print(c)
print(a * b) # element by element product
print(np.dot(a, b)) # aka scalar product
print(np.cross(a, b)) # aka vector product

# %%
# linear equation system solver demo:
#
# 8x + 3y -2z = 9
# -4x +7y + 5z = 15
# 3x + 4y - 12z = 35
#
coeff = [[8, 3, -2], [-4, 7, 5], [3, 4, -12]]
rightpart = [9, 15, 35]
answer = np.linalg.solve(coeff,rightpart)
x = answer[0]
y = answer[1]
z = answer[2]
print('x =', x, 'y =', y, 'z =', z)
# check if the solution is correct:
print(8*x + 3*y -2*z)
print(-4*x + 7*y +5*z)
print(3*x +4*y-12*z)

# %%
# matplotlib demos

x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)

plt.xlabel('x values')
plt.ylabel('y values')
plt.title('plotted x and y values')
plt.legend(['line 1'])


# save the figure
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()
# %%
# multiline plot demo
# object oriented approach

x = np.arange(0, 4*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)

fig, ax = plt.subplots() # NB: subplots, (!) not sublpot

ax.plot(x, y)
ax.plot(x, z)

ax.set_title('Two Trig Functions')
ax.legend(['sin','cos'])
ax.xaxis.set_label_text('Angle Θ')
ax.yaxis.set_label_text('Sine and Cosine')

plt.show()

# %%
# bar plots

# Data
Al = np.array([
    6.4e-5, 3.01e-5, 2.36e-5, 3.0e-5, 7.0e-5, 4.5e-5, 3.8e-5, 4.2e-5, 2.62e-5,
    3.6e-5
])
Cu = np.array([
    4.5e-5, 1.97e-5, 1.6e-5, 1.97e-5, 4.0e-5, 2.4e-5, 1.9e-5, 2.41e-5, 1.85e-5,
    3.3e-5
])
steel = np.array([
    3.3e-5, 1.2e-5, 0.9e-5, 1.2e-5, 1.3e-5, 1.6e-5, 1.4e-5, 1.58e-5, 1.32e-5,
    2.1e-5
])

mean_Al = np.mean(Al)
mean_Cu = np.mean(Cu)
mean_steel = np.mean(steel)

Al_std = np.std(Al)
Cu_std = np.std(Cu)
steel_std = np.std(steel)

materials = ['Al', 'Cu', 'Steel']
x_pos = np.arange(len(materials))
CTEs = [mean_Al, mean_Cu, mean_steel]
error = [Al_std, Cu_std, steel_std]


fig, ax = plt.subplots()

ax.bar(x_pos, CTEs, yerr=error, capsize=10, align='center', alpha=0.5)
ax.set_ylabel('Coefficient of Thermal Expansion, 1/C')
ax.set_xticks(x_pos)
ax.set_xticklabels(materials)
ax.set_title('Coefficients of Thermal Expansion of three materials')
ax.yaxis.grid(True)

plt.tight_layout()
plt.savefig('bar_plot.png')
plt.show()

# %%

