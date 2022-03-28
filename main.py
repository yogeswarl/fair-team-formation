import numpy as np
import pandas as pd
from common.author import Author
import matplotlib.pyplot as plt
from collections import Counter
df = pd.read_json('toy.v12.dblp.json')
working_df = pd.DataFrame(columns=["name", "id"])
Author_name, Author_id = [], []
for i,index in enumerate(df["authors"]):
    for j in index:
        Author_name.append(j["name"])
        Author_id.append(j["id"])
# x = Counter(Author_name)
# print(Counter(Author_name))
# x_reverse = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))
# plt.plot(list(Counter(x_reverse).values()))
# plt.show()
author_Instance = []
for _, index in enumerate(df["authors"]):
    for author in index:
        author_Instance.append(Author(author["name"], author["id"],df["fos"][_]))








