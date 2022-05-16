import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt

data = np.array([1, 2, 3, 4, 5, 6])
print(data)

one = np.random.choice(data, size=3, replace=True)
print(one)


for i in range(len(data)):
    one = np.random.choice(data, size=1, replace=False)
    print(one)

