CHAMP_HEURES_MAX = 23
CHAMP_MINUTES_MAX = 59
NB_MINUTES_MAX = 59

heures = int(input("Saisir le champ des heures : "))

if heures < 0 or heures > CHAMP_HEURES_MAX : # Vérification de la plage des heures
    print("Valeur du champ incorrecte.\nOpération annulée") # Si en dehors → erreur
else :
    minutes = int(input("Saisir le champ des minutes : ")) # Récupération de la saisie des minutes
    if minutes < 0 or minutes > CHAMP_MINUTES_MAX : # Vérification de la plage des minutes
        print("Valeur du champ incorrecte.\nOpération annulée") # Si en dehors → pas bon
    else :
        nb_minutes = int(input("Saisir le nombre de minutes : ")) # Récupération de la saisie des minutes à débiter
        if nb_minutes < 0 or nb_minutes > NB_MINUTES_MAX : # Vérification de la plage des minutes
            print("Valeur du champ incorrecte.\nOpération annulée") # Si en dehors de la place → false
        else : 
            minutes = minutes - nb_minutes # Soustraction des minutes
            if minutes < 0 :  # Si les minutes sont inférieures 0 →
                heures = heures - 1        # Décrémentation d'une heure 
                minutes = minutes + 60     # Incrémentation de 60 minutes

            if heures < 0 :
                heures = heures + 24

            print("Champ des heures :",heures) #On affiche "heures"
            print("Champ des minutes :",minutes) #On affiche "minutes"


            