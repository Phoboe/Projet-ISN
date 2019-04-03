import classes.joueur
import classes.display
import classes.gestion
from classes.locals import game_properties
from classes.locals import contenu

import os










class menu:
    def __init__(self):
        print("à ,l'intérieur du menu")
        pass

    i = 1
    for elt in contenu.Rules[1:15]: # on parcours les lignes du menu (règles)
        print(elt) # et on les affiche
        i += 1
        if i is 15:
            os.system("pause")
            i = 10




    pass


class main:
    def __init__(self):
        print("à l'intérieur du main")
        pass

    print("\nVotre rôle est : {0}\n".format(classes.joueur.define_role()))

    valid = False
    while valid is False:
        x = input('Voulez- vous commencer une partie ?\n')
        try:
            suite = suite.upper()
        except TypeError:
            print("Vérifiez que vous avez bien rentré une lettre.\n")
        else:
            if suite.upper() != "O" and suite.upper() != "N":
                print("vous devez rentrer un 'O' ou un 'N', pour Oui ou Non.")
            valid = True
        pass



    pass








if __name__ is '__main__':
    print('Lancement menu')
    menu()
    print('Lancement partie')
    main()
    print('Fin du jeu')








#os.system('cls')
os.system('echo Programme terminé avec succès.')
'''END'''
