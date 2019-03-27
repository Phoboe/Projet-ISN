#coding UTF-8

import classes.joueur
import classes.display
import classes.gestion
from classes.locals import game_properties







class localvars:
    def __init__(self):
        file = open("classes/locals/contenu.txt")
        self.lines = file.readlines()
        file.close()
        pass
localvars = localvars()



class menu:
    def __init__(self):
        print("à ,l'intérieur du menu")
        pass


    for elt in localvars.lines:
        print(elt[:-1])




    pass


class main:
    def __init__(self):
        print("à ,l'intérieur du main")
        pass

    print(classes.joueur.define_role())





    pass








if __name__ is '__main__':
    print('Lancement menu')
    menu()
    print('Lancement partie')
    main()
    print('Fin du jeu')









'''END'''
