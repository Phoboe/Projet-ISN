from random import randrange
import classes.locals.game_properties

state = True # l'état de vie ou de mort du joueur

def define_role():
    if classes.locals.game_properties.customize == True:
        pass
    alea = randrange(0, 24, 1)
    if alea >= 0 and alea <= 3: role = 'loupgarou'
    elif alea >= 4 and alea <= 17: role = 'vilageois'
    elif alea == 18: role = 'voyante'
    elif alea == 19: role = 'voleur'
    elif alea == 20: role = 'chasseur'
    elif alea == 21: role = 'cupidon'
    elif alea == 22: role = 'sorciere'
    elif alea == 23: role = 'petitefille'
    elif alea == 24: role = 'maire'
    return role























'''end'''
