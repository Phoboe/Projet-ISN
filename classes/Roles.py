class Loup_garou():
    """Classe du loup garou."""
    def __init__.py
    self.text = ["Les loups garous se réveillent",
    "Ils choisissent leur victime"]

class Villageois():
    """Classe du villageois."""
    def __init__(self):
        pass
    self.text = ["Les villageois votent"]

class Sorciere():
    """Classe de la sorcière."""
    def __init__(self):
        pass
    self.text = ["La sorcière se réveille",
    "Elle prend connaissance de la victime",
    "Elle peut la sauver, tuer quelqu'un d'autre ou ne rien faire",
    "La sorcière agit et se rendort"]

class Voleur():
    """Classe du voleur."""
    def __init__(self):
        pass
    self.text = ["Le voleur se réveille",
    "Le voleur choisit entre 2 cartes non utilisées et change de role",
    "le voleur a choisi son nouveau role se rendort"]

class Cupidon():
    """Classe de cupidon."""
    def __init__(self):
        pass
    self.text = ["Cupidon se réveille",
    "Il choisit 2 joueurs qui sont liés par l'amour",
    "Cupidon se rendort"]

class Petite_fille():
    """Classe de la petite fille."""
    def __init__(self):
        pass
    self.text = ["La petite fille se réveille et voit un des loups garous",
    "La petite fille se rendort"]

class Voyante():
    """Classe de la voyante."""
    def __init__(self):
        pass
    self.text = ["La voyante se réveille",
    "Elle choisit quelqu'un dont elle souhaite connaître l'identité",
    "La voyante se rendort"]

class Chasseur():
    """Classe du chasseur."""
    def __init__(self):
        pass
    self.text = ["Le chasseur est mort et tire sa dernière balle"]

class Maire():
    """Classe du maire."""
    def __init__(self):
        pass
    self.text = ["Le maire vote"]





def define_role():


    liste = [
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

    for i in range(0, 80):
        listeStart = []
        listeEnd = []
        alea = randrange(1, 18, 1)
        listeStart = liste[:(alea)]
        listeEnd = liste[(alea+1):18]
        replace = liste[alea]
        liste[:] = []
        liste.append(replace)
        liste += listeStart
        liste += listeEnd
        pass

    roles = liste
    """
    for i in range(0, 18,1):
        #print(i)
        print(liste[i])"""

    return roles





'''END'''
