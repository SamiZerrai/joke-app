# Créez un décorateur:

# qui se nommera censorship
# pour une fonction qui ne prend pas de paramètres, et qui retourne une str
# qui remplacera les mots "libre" et "dictature" (insensibles à la casse) par des séries de "_" de même taille.
# Exemple d'utilisation : 

# @censorship
# def annonce():
#     return "Un pays LIBRE de toute dictature"
# print(annonce()) #affiche "Un pays ____ de toute _________"

def censorship(func):
    def wrapper():
        return func().replace("libre", "____").replace("dictature", "_________")
    return wrapper