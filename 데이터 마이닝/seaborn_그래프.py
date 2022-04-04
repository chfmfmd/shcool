import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fish_multi = pd.read_csv("./data/3-3-2-fish_multi_2.csv")
print(fish_multi)

fish_multi_group = fish_multi.groupby("species")
print(fish_multi_group)
print(fish_multi_group.describe())

print(fish_multi_group.count())
want_cols = ["species", "length"]
print(fish_multi[want_cols])

print(fish_multi[1:3]["species"])
print(fish_multi.loc[1:3, "species"])

print(fish_multi[fish_multi["species"] == "A"])
# print(fish_multi["species"] == "A")
print(fish_multi[fish_multi.species == "A"][0:3]["length"])
print(fish_multi[fish_multi.species == "A"].loc[0:2, "length"])

print(fish_multi.query("species == 'A'")["length"])
