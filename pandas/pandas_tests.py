import numpy as np
import pandas as pd
from numpy.random import randn

# labels = ['a', 'b', 'c']
# my_data = [10, 20, 30]
# arr = np.array(my_data)
# d = {'a':10, 'b':20, 'c':30}

# print(pd.Series(data = my_data, index=labels))

# ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])
# ser2 = pd.Series([1,2,5,4], ['USA', 'Germany', 'Italy', 'Japan'])

np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
df['New'] = df['W'] + df['Y']
#df.loc for rows, and df['Name'] for cols
# print(df.loc['A'])
# print(df[df > 0])

boolser = df['W'] > 0
result = df[boolser]

print(df[(df['W'] > 0) & (df['Y'] > 1)])