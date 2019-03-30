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
    for elt in contenu.lines[2:20]: # on parcours les lignes du menu (règles)
        print(elt) # et on les affiche
        i += 1
        if i is 15:
            print('\n----------------------------------------')
            os.system("pause")
            print('----------------------------------------\n')
            i = 10




    pass


class main:
    def __init__(self):
        print("à ,l'intérieur du main")
        pass

    print("\nVotre rôle est : {1}\n".format(classes.joueur.define_role()))





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
