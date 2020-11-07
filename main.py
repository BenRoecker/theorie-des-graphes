# coding : utf-8
import graphes

if __name__ == '__main__':
    choix = -1
    choix = input("Quelles graphes orientés voulez vous choisir ? tapez fin pour arreter")
    while choix != "fin":
        try:
            choix = int(choix)
        except:
            choix = 0
        while choix < 1 or choix > 13:
            choix = input("Il n'y a que 13 graphes. ")
            try:
                choix = int(choix)
            except:
                choix = 0
        choix = str(choix)
        texte = "graphes/graphe_" + choix + ".txt"
        cool = graphes.Graphe(texte)
        cool.matrice_adj()
        cool.floyd_warshall()
        choix = input("Quelles graphes orientés voulez vous choisir ? tapez fin pour arreter")

