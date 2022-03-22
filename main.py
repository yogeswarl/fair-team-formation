import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
df = pd.read_json('toy.v12.dblp.json')
working_df = pd.DataFrame(columns=["name", "id"])
name, id = [], []
for i,index in enumerate(df["authors"]):
    for j in index:
        name.append(j["name"])
        id.append(j["id"])
new_dest = dict(zip(name, id))
x = Counter(name)
# y = np.sin(x)
Counter(name).values()

x_reverse = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))
plt.plot(Counter(x_reverse).values())
plt.show()