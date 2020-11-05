# coding : utf-8
import graphes

if __name__ == '__main__':
    choix = -1
    while choix < 0 or choix > 50:
        choix = input("Quelles graphes non-orientés voulez vous choisir ?")
        try:
            choix = int(choix)
        except:
            choix = 0
    choix = str(choix)
    texte = "graphes/graphe_" + choix + ".txt"
    cool = graphes.Graphe(texte)
    cool.matrice_adj()
    cool.floyd_warshall()

