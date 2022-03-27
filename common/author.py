class Author(object):
    count = 0
    def __init__(self, id, name):
        Author.count += 1
        self.id = id
        self.name = name
        self.teams = set()
        self.skills = set()