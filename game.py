import random

score_user = 0
score_machine = 0
max_score = None

HANDS = ["pierre", "feuille", "ciseaux"]

# Jouer tant que l'un des joueurs n'a pas gagné 3 manches
while max_score != 3:

    # L'utilisateur choisit entre pierre, feuille ou ciseaux
    choice_user = input("Choisissez entre Pierre, Feuille ou Ciseaux ")

    # Vérifier que l'utilisateur choisit bien pierre, feuille ou ciseaux
    if choice_user in HANDS:

        # La machine tire au hasard
        choice_machine = random.choice(HANDS)

        # On compare les résultats et on le stock
        if choice_machine == "pierre" and choice_user == "ciseaux":
            score_machine += 1
        elif choice_machine == "pierre" and choice_user == "feuille":
            score_user += 1
        elif choice_machine == "ciseaux" and choice_user == "feuille":
            score_machine +=1
        elif choice_machine == "ciseaux" and choice_user == "pierre":
            score_user += 1
        elif choice_machine == "feuille" and choice_user == "pierre":
            score_machine +=1
        elif choice_machine == "feuille" and choice_user == "ciseaux":
            score_user +=1
        else:
            print("égalité")

    else:
        print(f"Choisis parmis pierre, feuille ou ciseaux")
        continue

    print(f"Utilisateur : {choice_user} - Machine : {choice_machine}")
    print(f"Utilisateur : {score_user} - Machine : {score_machine}")
    max_score = max(score_user, score_machine)
    print(max_score)

if max_score == score_user and max_score > 0:
    print("Bravo, c'est gagné")
else:
    print("Dommage... la prochaine sera la bonne!")
