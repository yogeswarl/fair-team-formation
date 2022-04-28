import pickle
import numpy as np
import json
from common.author import Author
from common.plot import plot_stats
from collections import Counter
from common.reranking import reranking_logic
from team_formation import form_teams_with_skills
from team_formation import convert_author_id_to_attributes
from experiment.experiment import experimental_metrics
print('loading DF')
author_Instance =list()
author_id = list()
# with open('data/toy.v12.dblp.json', "r", encoding='utf-8') as jf:
#     for line in jf:
#         try:
#             if not line: break
#             jsonline = json.loads(line.lower().lstrip(","))
#             id = jsonline['id']
#
#             try:fos = jsonline['fos']
#             except:continue
#             try:authors = jsonline['authors']
#             except:continue
#         except json.JSONDecodeError as e:  # ideally should happen only for the last line ']'
#             print(f'JSONDecodeError: There has been error in loading json line `{line}`!\n{e}')
#             continue
#         except Exception as e:
#             raise e
#         for author in authors:
#             author_Instance.append(Author(author["name"],author["id"], fos, authors))
#             author_id.append(author["id"])
print('loaded DF')
team_size = 4

# plot_stats(author_id)
list_of_skills = ["deep_learning"]
def load_data(indexes_path,teamsvec_path,list_of_skills):
    author_id = list()
    with open(indexes_path, 'rb') as infile:
        indexes = pickle.load(infile)
    with open(teamsvec_path, 'rb') as tfile:
        vecs = pickle.load(tfile)

    list_of_skill_vecs = list()
    for skill_item in list_of_skills:
        list_of_skill_vecs.append(indexes['s2i'][skill_item])
    author_list = list()
    for r in range(vecs["skill"].shape[0]):
        for c, d in zip(vecs["skill"].rows[r], vecs["skill"].data[r]):
            author_id.append(vecs["member"].rows[r])
            if c in list_of_skill_vecs:
                author_list.append(vecs["member"].rows[r])
    return np.concatenate(author_list), np.concatenate(author_id)
author_list,author_id = load_data(indexes_path='data/processed/dblp-toy/indexes.pkl',teamsvec_path='data/processed/dblp-toy/teamsvecs.pkl',list_of_skills=list_of_skills)
# item_attributes,author_id_to_dictionary = form_teams_with_skills(list_of_skills,author_Instance,author_list)
author_id_to_dictionary = convert_author_id_to_attributes(author_id,author_list)
author_id_list = list(Counter(author_id_to_dictionary).values())
item_attributes_reranked,distribution_list = reranking_logic(author_id_list,team_size,len(author_id),author_list,author_id_to_dictionary)
experimental_metrics(author_id_list,item_attributes_reranked,distribution_list)