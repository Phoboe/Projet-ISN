from random import randrange


class Loup_garou():
    """Classe du loup garou."""
    def __init__(self):
        self.text = ["Les loups garous se réveillent",
        "Ils choisissent leur victime"]

class Villageois():
    """Classe du villageois."""
    def __init__(self):
        self.text = ["Les villageois votent"]
        pass

class Sorciere():
    """Classe de la sorcière."""
    def __init__(self):
        self.text = ["La sorcière se réveille",
        "Elle prend connaissance de la victime",
        "Elle peut la sauver, tuer quelqu'un d'autre ou ne rien faire",
        "La sorcière agit et se rendort"]
        pass

class Voleur():
    """Classe du voleur."""
    def __init__(self):
        self.text = ["Le voleur se réveille",
        "Le voleur choisit entre 2 cartes non utilisées et change de role",
        "le voleur a choisi son nouveau role se rendort"]
        pass

class Cupidon():
    """Classe de cupidon."""
    def __init__(self):
        self.text = ["Cupidon se réveille",
        "Il choisit 2 joueurs qui sont liés par l'amour",
        "Cupidon se rendort"]
        pass

class Petite_fille():
    """Classe de la petite fille."""
    def __init__(self):
        self.text = ["La petite fille se réveille et voit un des loups garous",
        "La petite fille se rendort"]
        pass

class Voyante():
    """Classe de la voyante."""
    def __init__(self):
        self.text = ["La voyante se réveille",
        "Elle choisit quelqu'un dont elle souhaite connaître l'identité",
        "La voyante se rendort"]
        pass

class Chasseur():
    """Classe du chasseur."""
    def __init__(self):
        self.text = ["Le chasseur est mort et tire sa dernière balle"]
        pass

class Maire():
    """Classe du maire."""
    def __init__(self):
        self.text = ["Le maire vote"]
        pass



def mix(list, times):
    ''' mix the list's elements'''
    for i in range(0, (times + 1)):
        listStart = []
        listEnd = []
        alea = randrange(1, 18, 1)
        listStart = list[:(alea)]
        listEnd = list[(alea+1):18]
        replace = list[alea]
        list[:] = []
        list.append(replace)
        list += listStart
        list += listEnd
        pass
    return list

def define_role():


    roles = [
    'loup garou',
    'loup garou',
    'loup garou',
    'loup garou',
    'villageois',
    'villageois',
    'villageois',
    'villageois',
    'villageois',
    'villageois',
    'villageois',
    'voleur',
    'cupidon',
    'petite fille',
    'voyante',
    'chasseur',
    'maire',
    'sorciere'   ]


    roles = mix(roles, 160) # on mixe la liste 160 fois



    return roles





'''END'''
