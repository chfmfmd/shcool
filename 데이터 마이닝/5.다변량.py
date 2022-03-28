import pandas as pd

fish_multi = pd.read_csv("./data/3-2-1-fish_multi.csv")
print(type(fish_multi))
print(fish_multi)

group = fish_multi.groupby("species")
print(group.mean())
print(group.max())
print(group.min())
print(group.std(ddof = 1))

print(group.describe())

shoes = pd.read_csv("./data/3-2-2-shoes.csv")
print(type(shoes))
cross = pd.pivot_table(
 data = shoes,
 values = "sales",
 aggfunc = "sum",
 columns = "color")
print(cross)

store_cross = pd.pivot_table(
 data = shoes,
 values = "sales",
 aggfunc = "sum",
 columns = "store")
print(store_cross)
#공분산







