import numpy as np
import pandas as pd
from common.author import Author
from common.plot import plot_stats
from collections import Counter
from common.reranking import reranking_logic
from team_formation import form_teams_with_skills
from experiment.experiment import experimental_metrics
df = pd.read_json('toy.v12.dblp.json')
plot_stats(df)
team_size = 4
# store list of author classes
author_Instance =list()
for _, index in enumerate(df["authors"]):
    for author in index:
        author_Instance.append(Author(author["name"], author["id"], df["fos"][_], index))
list_of_skills = ["deep_learning"]
author_id = list()
for author in author_Instance:
    author_id.append(Author.get_author_id(author))
item_attributes,author_id_to_dictionary = form_teams_with_skills(list_of_skills,author_Instance,author_id)
author_id_list = list(Counter(author_id_to_dictionary).values())
item_attributes_reranked,distribution_list = reranking_logic(author_id_list,team_size,len(author_Instance),author_id,author_id_to_dictionary)
experimental_metrics(author_id_list,item_attributes_reranked,distribution_list)