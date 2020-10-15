# coding : utf-8

def creer_graphe(document):
    ligne = document.split("\n")  # découpe ne texte en tableau à l'aide des retour à la ligne
    tab_arcs = []
    for i in range(2, 2 + int(ligne[1])):
        tab_arcs.append(ligne[i])  # ajout de chaque arc dans le tableau
    for i in range(0, int(ligne[1])):
        tab_arcs[i] = tab_arcs[i].split(" ")  # division de chaque en arc en donnée. 0.initial 1.terminal 3.valeur
        tab_arcs[i][2] = int(tab_arcs[i][2])  # transformation de la dernière donnée en valeur numérique
    return [ligne, tab_arcs]


class Graphe:
    def __init__(self, document):
        print("C R E A T I O N   A U T O M A T E")
        document = open(document, "r")
        fichier = document.read()
        [ligne, tab_graphes] = creer_graphe(fichier)
        self.nombre_sommet = int(ligne[0])
        self.nombre_arc = int(ligne[1])
        self.arcs = tab_graphes
        document.close()

