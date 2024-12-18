import random

# Étape 1 : Préparation

longueur_comb = 4
essaies_maximum = 10
couleurs = ["Vert", "Noir", "Rouge", "Jaune", "Orange", "Marron"]

# Étape 2 : 
def combinaison_secrete():
    return [random.choice(couleurs) for _ in range(longueur_comb)]

# Étape 3 : 
def recuperer_proposition():
    while True:
        demande = input(f"Entrer une combinaison de {longueur_comb} couleurs parmi {', '.join(couleurs)}: ")
        try:
            proposition = demande.split()
            if len(proposition) != longueur_comb:
                raise ValueError(f"Il faut entrer exactement {longueur_comb} couleurs.")
            if not all(couleur in couleurs for couleur in proposition):
                raise ValueError(f"Les couleurs doivent appartenir à : {', '.join(couleurs)}.")
            return proposition
        except ValueError as e:
            print(f"Entrée invalide : {e}")

# Étape 4 : Vérifier la proposition
def check_proposition(solution, proposition):
    val_bien_placées = sum(s == p for s, p in zip(solution, proposition))
    val_mal_palcées = 0

    # Vérifier les doublons
    solution_differente = []
    proposition_differente = []

    for s, p in zip(solution, proposition):
        if s != p:
            solution_differente.append(s)
            proposition_differente.append(p)

    # Compter les couleurs mal placées
    for couleur in proposition_differente:
        if couleur in solution_differente:
            val_mal_palcées += 1
            solution_differente.remove(couleur)

    return val_bien_placées, val_mal_palcées

# Étape 5 : Lancer le jeu
def commencer_le_jeu():
    print("Bienvenue sur ton MASTERMIND !")
    solution = combinaison_secrete()

    nombre_essais = essaies_maximum

    while nombre_essais > 0:
        print(f"\nIl vous reste {nombre_essais} essais !")
        proposition = recuperer_proposition()
        val_bien_placées, val_mal_placées = check_proposition(solution, proposition)

        print(f"Résultat : {val_bien_placées} bien placée(s), {val_mal_placées} mal placée(s).")

        if val_bien_placées == longueur_comb:
            print("Félicitations, vous avez gagné !")
            return

        nombre_essais -= 1

    # Si tous les essais sont épuisés
    print(f"\nOh non, tous les essais sont épuisés.")
    print(f"La combinaison secrète était : {', '.join(solution)}")

# Étape 6 : Lancer le programme si exécuté directement
if __name__ == "__main__":
    commencer_le_jeu()
