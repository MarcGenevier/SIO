CHAMP_HEURES_MAX = 23
CHAMP_MINUTES_MAX = 59
NB_MINUTES_MAX = 59
heures = int(input("Saisir champ heures :")) # récupération saisie des heures

if heures < 1 or heures > CHAMP_HEURES_MAX : # on vérifie la plage des heures
    print("Valeur du champ heures incorrectes.\n Opération annulée.") # si l'utilisateur ne respecte pas opé annulée
else : 
    minutes = int(input("Saisir champ minutes :")) # on vérifie la plage des minutes
    if minutes < 1 or minutes > CHAMP_MINUTES_MAX : # délimitation des minutes maximum 
        print("Valeur du champ des heures incorrectes.\n Opération annulée.") # si l'user ne respecte pas opé annulée
    else :
        nb_minutes = int(input("Saisir le nombre de minutes à déduire :")) # on vérifie la plage des minutes à déduire
        if nb_minutes < 1 or nb_minutes > NB_MINUTES_MAX : # délimitation des minutes à déduire
            print("Nombre de minutes incorrectes.\n Opération annulée.") # si l'user ne respecte pas opé annulée 
        else:
            minutes = minutes - nb_minutes  # on déduit à minutes le nombre de minutes à déduire
            if minutes < 0 : # si les minutes sont inférieur à 0 :
                heures = heures - 1 # Décrémentation d'une heure
                minutes = minutes + 60 # Incrémentation de 60 minutes 
            
            if heures < 0 :
                heures = + 24

            print("Champ des heures", heures)
            print("Champ des minutes", minutes)    
                
     