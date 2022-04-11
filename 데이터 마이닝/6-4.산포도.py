import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp

cov_data = pd.read_csv("./data/3-2-3-cov.csv")
print(cov_data)

x = cov_data["x"]
y = cov_data["y"]
print(cov_data.columns)
print(cov_data.index)

scipy_cov = np.cov(x, y, ddof=1)
print(scipy_cov)
# 피어슨 상관 계수
corre = np.corrcoef(x, y, ddof=1)
print(corre)

sns.jointplot(x="x", y="y", data=cov_data, color="black")
plt.show()