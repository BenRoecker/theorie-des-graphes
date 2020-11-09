# coding : utf-8

def creer_graphe(document):
    ligne = document.split("\n")  # découpe ne texte en tableau à l'aide des retour à la ligne
    tab_arcs = []
    for i in range(2, 2 + int(ligne[1])):
        tab_arcs.append(ligne[i].split(" "))  # ajout de chaque arc dans le tableau
    return [ligne, tab_arcs]  # on retourne toutes les lignes ainsi que le tableau d'arcs crées


class Graphe:
    def __init__(self, document):
        print("C R E A T I O N   A U T O M A T E")
        document = open(document, "r")  # Ouverture du document
        fichier = document.read()  # lecture du document
        [ligne, tab_graphes] = creer_graphe(fichier)
        self.nombre_sommet = int(ligne[0])
        self.nombre_arc = int(ligne[1])
        self.arcs = tab_graphes
        document.close()  # fermeture du document

    def matrice_adj(self):
        print("MATRICE D'ADAJACENCE")
        taille_max = 0  # variable donnant le nombre d'espace à rajouter dans chaque case
        for arcs in self.arcs:
            for valeur in arcs:
                if len(valeur) >= taille_max:
                    taille_max = len(valeur)  # Cherche la plus grand longueur de valeur et l'affecte à taille_max
        # Affichage de la première ligne
        print(" "*taille_max, end="|")
        for i in range(self.nombre_sommet):
            espace = taille_max - len(str(i))
            print(str(i) + (" "*espace), end="|")
        print("")
        # Affichage du reste du tableau
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

    # Permet de savoir si un arc existe et retourne sa position dans le tableau donnée en paramètre
    def existence_arcs(self, init, term, tab):
        for i in range(len(tab)):
            if tab[i][0] == init and tab[i][1] == term:
                return [tab[i][2], i]
        return ["-", ""]

    def existence_chemin(self, init, term, chemin):
        for i in range(len(chemin)):
            if init == chemin[i][0] and term == chemin[i][len(chemin[i])-1]:
                return i

    def floyd_warshall(self):
        print("ALGORITHME DE FLOYD-WARSHALL")
        etat = 0
        chemin = []
        for i in self.arcs:
            chemin.append([i[0], i[1]])
        changement = True
        print("ETAT INITIAL")
        print("Chemins :" + str(chemin))
        self.matrice_adj()  # le tableau de transition contient tout les arcs
        while changement:
            transition = []
            transition = transition + self.arcs
            etat += 1
            changement = False
            for arcs in self.arcs:
                for thing in self.arcs:
                    if arcs[1] == thing[0]:  # Si l'état terminal d'un arc == l'état initial d'un arc
                        [new_val, id] = self.existence_arcs(arcs[0], thing[1], transition)  # existence de la somme des 2 arcs
                        if new_val == "-":  # s'il n'existe pas
                            transition.append([arcs[0], thing[1], str(int(arcs[2])+int(thing[2]))])  # on l'ajoute dans le tableau
                            index = self.existence_chemin(arcs[0], arcs[1], chemin)
                            index_part = self.existence_chemin(thing[0], thing[1], chemin)
                            trans = []
                            trans = trans + chemin[index]
                            del trans[-1]
                            print("ajout du chemin :", trans+chemin[index_part] )
                            chemin.append(trans+chemin[index_part])
                            changement = True
                        elif int(new_val) > int(arcs[2])+int(thing[2]):  # si la somme des valeurs est inférieur à une valeur déjà calculé
                            index = self.existence_chemin(arcs[0], thing[1], chemin)
                            new_indexpart = self.existence_chemin(thing[0], thing[1], chemin)
                            partnew_index = self.existence_chemin(arcs[0], arcs[1], chemin)
                            trans = []
                            trans = trans + chemin[partnew_index]
                            del trans[-1]
                            print("Modification du chemin :", chemin[index], "-->", trans+chemin[new_indexpart])
                            chemin[index] = trans+chemin[new_indexpart]
                            transition[id][2] = str(int(arcs[2])+int(thing[2]))  # on remplace cette valeur
            # test de présence de cycle absorbant
            cycle_absorbant = False
            print("Chemins :" + str(chemin))
            for i in range(self.nombre_sommet):
                valeur = self.existence_arcs(str(i), str(i), transition)[0]  # Recherche les valeurs dans la diagonale
                if valeur != "-":
                    if int(valeur) < 0:  # Si cette valeur est inférieur à 0 alors
                        cycle_absorbant = True  # Il existe un cycle absorbant
                        changement = False  # on arrête l'algorithme
            if cycle_absorbant:
                print("Il existe un cycle absorbant")
            print("ETAPE n°" + str(etat+1))
            self.arcs = transition
            self.matrice_adj()
