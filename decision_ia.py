import sklearn
from sklearn import tree

def insect_choice(insect_array):
    formiga = 1
    abelha = 2
    mosca = 3

    learn_data = [
        [0, 0, 0, 0, 0, 0, formiga, 1853, 540],
        [abelha, 1853, 540, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, mosca, 1853, 540, 0, 0, 0],

        [mosca, 1853, 540, abelha, 1853, 540, 0, 0, 0],
        [mosca, 1853, 540, formiga, 1853, 540, 0, 0, 0],
        [mosca, 700, 540, mosca, 1853, 540, 0, 0, 0],

        [abelha, 1853, 540, formiga, 1853, 540, 0, 0, 0],
        [abelha, 1853, 540, mosca, 1853, 540, 0, 0, 0],
        [abelha, 700, 540, abelha, 1853, 540, 0, 0, 0],

        [formiga, 1853, 540, abelha, 1853, 540, 0, 0, 0],
        [formiga, 1853, 540, mosca, 1853, 540, 0, 0, 0],
        [formiga, 700, 540, formiga, 1853, 540, 0, 0, 0],
    ]

    learn_clicks = [
        [formiga, 1853, 540],
        [abelha, 1853, 540],
        [mosca, 1853, 540],

        [abelha, 1853, 540],
        [formiga, 1853, 540],
        [mosca, 1853, 540],

        [formiga, 1853, 540],
        [abelha, 1853, 540],
        [abelha, 1853, 540],

        [formiga, 1853, 540],
        [formiga, 1853, 540],
        [formiga, 1853, 540],
    ]

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(learn_data, learn_clicks)

    decision = clf.predict([insect_array])
    return decision[0]

