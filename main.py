import numpy as np
import pandas as pd
from common.author import Author
from common.plot import plot_stats

df = pd.read_json('toy.v12.dblp.json')
working_df = pd.DataFrame(columns=["name", "id"])
plot_stats(df)
author_Instance = []
for _, index in enumerate(df["authors"]):
    for author in index:
        author_Instance.append(Author(author["name"], author["id"],df["fos"][_],index))
print(type(author_Instance[0].get_skills()))


