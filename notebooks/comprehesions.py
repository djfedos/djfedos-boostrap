# Following this video tutorial: https://youtu.be/3dt4OGnU5sM

# %%
from distutils.ccompiler import gen_lib_options


my_list = [n for n in range(11) if n%2 != 0]
print(my_list)
# %%
my_list = [(m,n) for m in range(10) for n in range(10)]
print(my_list)
# %%
# dict comprehension using zip function
musicians = ['Ian Gillan', 'Ian Paice', 'Roger Glover', 'Jon Lord', "Ritchie Blackmore"]
instruments = ['Voice', 'Drums', 'Bass', 'Keyboards', 'Guitar']

band = {musician:instrument for musician, instrument in zip(musicians, instruments)}
print(band)
# %%
# generator in comprehesion-like style
my_gen = (n for n in range(11) if n%2 == 0)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
# %%
matrix_gen = ((m,n) for m in range(10) for n in range(10))
for pair in matrix_gen:
    print(pair)
# %%

