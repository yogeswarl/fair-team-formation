class Author(object):
    count = 0

    def __init__(self, name, id,fos):
        Author.count += 1
        self.id = id
        self.name = name
        self.fos = fos
        self.teams = set()
        self.skills = self.set_skills()

    def set_author_popularity(self):
        return self.id

    def set_skills(self):
        skills = set()
        for skill in self.fos:
            skills.add(skill["name"].replace(" ", "_"))
        return skills

    def get_skills(self):
        return self.skills