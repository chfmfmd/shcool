import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = pd.read_csv("./data/sample_data.csv")
print(x)

x_group = x.groupby("col2")
print(x_group)
print(x_group.describe())

print(x_group.count())
want_cols = ["col2", "col1"]
print(x[want_cols])

print(x[1:3]["col2"])
print(x.loc[1:3, "col2"])

print(x[x["col2"] == "C"])
print(x[x.col2 == "C"][0:7]["col1"])
print(x[x.col2 == "C"].loc[0:6, "col1"])

print(x.query("col2 == 'C'")["col1"])