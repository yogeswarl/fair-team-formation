import numpy as np
import json
from common.author import Author
from common.plot import plot_stats
from collections import Counter
from common.reranking import reranking_logic
from team_formation import form_teams_with_skills
from experiment.experiment import experimental_metrics
print('loading DF')
author_Instance =list()
author_id = list()
with open('toy.v12.dblp.json', "r", encoding='utf-8') as jf:
    for line in jf:
        try:
            if not line: break
            jsonline = json.loads(line.lower().lstrip(","))
            id = jsonline['id']
            title = jsonline['title']
            year = jsonline['year']
            type = jsonline['doc_type']
            venue = jsonline['venue'] if 'venue' in jsonline.keys() else None
            references = jsonline['references'] if 'references' in jsonline.keys() else []
            keywords = jsonline['keywords'] if 'keywords' in jsonline.keys() else []


            try:fos = jsonline['fos']  # an array of (name, w), w shows a weight. Not sorted! Can be used later!
            except:continue  # publication must have fos (skills)
            try:authors = jsonline['authors']
            except:continue  # publication must have authors (members)
            #         author_Instance.append(Author(author["name"], author["id"], df["fos"][_], index))
            #         author_id.append(author["id"])
        except json.JSONDecodeError as e:  # ideally should happen only for the last line ']'
            print(f'JSONDecodeError: There has been error in loading json line `{line}`!\n{e}')
            continue
        except Exception as e:
            raise e
        print(line)
        #         author_Instance.append(Author(author["name"], author["id"], df["fos"][_], index))
        #         author_id.append(author["id"])
print('loaded DF')
team_size = 4
# store list of author classes
# author_Instance =list()
# author_id = list()
# for _, index in enumerate(df["authors"]):
#     for author in index:
#         author_Instance.append(Author(author["name"], author["id"], df["fos"][_], index))
#         author_id.append(author["id"])
plot_stats(author_id)
list_of_skills = ["deep_learning"]
item_attributes,author_id_to_dictionary = form_teams_with_skills(list_of_skills,author_Instance,author_id)
author_id_list = list(Counter(author_id_to_dictionary).values())
item_attributes_reranked,distribution_list = reranking_logic(author_id_list,team_size,len(author_Instance),author_id,author_id_to_dictionary)
experimental_metrics(author_id_list,item_attributes_reranked,distribution_list)