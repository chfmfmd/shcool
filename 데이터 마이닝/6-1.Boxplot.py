import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fish_multi = pd.read_csv("./data/3-3-2-fish_multi_2.csv")
print(fish_multi)

fish_a = fish_multi[fish_multi.species == "A"]  # = fish_multi[fish_multi["species"] == "A"]
fish_b = fish_multi.query("species == 'B'")

sns.boxplot(data=fish_multi, x="species", y="length", color="blue")
plt.show()