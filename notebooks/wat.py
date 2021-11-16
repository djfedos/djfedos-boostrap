
#%%
#The undocumented converse implication operator
print(False ** False == True)
print(False ** True == False)
print(True ** False == True)
print(True ** True == True)
print("")
#explanation:
print(0 ** 0)
print(0 ** 1)
print(1 ** 0)
print(1 ** 1)
# %%
x = (1 << 53) + 1
print(x + 1.0 < x)
print("")
#explanation:
print(float(x))
print(x + 1.0)
print(x)
#x is a smallest whole number that can't be represented exactly 
# as a python float and gets rounded to the nearest value
# comparison in Python does not convert numbers between types
# %%
print(False == False in [False])
#explanation: it's equivalent to
print((False == False) and (False in [False]))
# %%
print(type(1 ** 1))
print(type(1 ** -1))

# %%
a = 2, 1, 3
print(sorted(a) == sorted(a))
print(reversed(a))
#reversed function returns an iterator, not a list
# %%
