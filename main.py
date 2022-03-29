import numpy as np
import pandas as pd
from common.author import Author
from common.plot import plot_stats
from collections import Counter
from common.reranking import reranking_logic
from team_formation import form_teams_with_skills

df = pd.read_json('toy.v12.dblp.json')
plot_stats(df)

# store list of author classes
author_Instance = []
for _, index in enumerate(df["authors"]):
    for author in index:
        author_Instance.append(Author(author["name"], author["id"], df["fos"][_], index))
list_of_skills = ["image_processing","deep_learning"]
distribution_list,item_attributes =form_teams_with_skills(list_of_skills,author_Instance)
reranking_logic(item_attributes,distribution_list,2)