# coding : utf-8

def creer_graphe(document):
    ligne = document.split("\n")  # découpe ne texte en tableau à l'aide des retour à la ligne
    tab_arcs = []
    for i in range(2, 2 + int(ligne[1])):
        tab_arcs.append(ligne[i])  # ajout de chaque arc dans le tableau
    for i in range(0, int(ligne[1])):
        tab_arcs[i] = tab_arcs[i].split(" ")  # division de chaque en arc en donnée. 0.initial 1.terminal 3.valeur
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

    def matrice_adj(self):
        print("MATRICE D'ADAJACENCE")
        taille_max = 0
        for arcs in self.arcs:
            for valeur in arcs:
                if len(valeur) >= taille_max:
                    taille_max = len(valeur)
        print(" "*taille_max, end="|")
        for i in range(self.nombre_sommet):
            espace = taille_max - len(str(i))
            print(str(i) + (" "*espace), end="|")
        print("")
        for i in range(self.nombre_sommet):
            espace = taille_max - len(str(i))
            print(str(i) + (" " * espace), end="|")
            for j in range(self.nombre_sommet):
                presence = False
                for arcs in self.arcs:
                    if arcs[0] == str(i) and arcs[1] == str(j):
                        espace = taille_max - len(arcs[2])
                        print(arcs[2] + (" " * espace), end="|")
                        presence = True
                if not presence:
                    print("-" + (" "*(taille_max-1)), end="|")
            print("")

    def floyd_warshall(self):
        print("ALGORITHME DE FLOYD-WARSHALL")
        etat = 0
        changement = True
        print("ETAT INITIAL")
        self.matrice_adj()
        transitions = self.arcs
        while changement:
            etat += 1
            for arcs in transitions:
                for things in self.arcs:
                    if arcs[1] == things[0]:
                        #  à terminer


