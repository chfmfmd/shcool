import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
# print(iris)
# print(type(iris))
# print(iris.columns)
sns.pairplot(iris, hue="species", palette="husl")
plt.show()
