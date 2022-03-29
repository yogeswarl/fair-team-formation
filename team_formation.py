def get_distribution(authorList):
    distribution_list = {}
    distribution_value = (100/len(list(set(authorList))))/100
    for author in list(set(authorList)):
        distribution_list[author] = distribution_value
    return distribution_list

def form_teams_with_skills(list_of_skills, author_Instance):
    list_of_skills = [list.title() for list in list_of_skills]
    author_list = []
    for list in list_of_skills:
        for author in author_Instance:
            if list in author.get_skills():
                author_list.append(author.id)
    distribution_list = get_distribution(author_list)
    print(author_list)
    print(distribution_list)
    return distribution_list, author_list

