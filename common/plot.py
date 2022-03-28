from collections import Counter
import matplotlib.pyplot as plt
Author_name, Author_id = [], []
def plot_stats(df):
    for i, index in enumerate(df["authors"]):
        for j in index:
            Author_name.append(j["name"])
            Author_id.append(j["id"])
    x = Counter(Author_name)
    print(Counter(Author_name))
    x_reverse = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))
    plt.plot(list(Counter(x_reverse).values()))
    plt.xlabel("Number of Authors")
    plt.ylabel("Number of labels published")
    plt.show()