from monster import monster

class bear(monster):   
    def __init__(self, name="8 F***ing bears", description="They're 8 bears", basicName="Claw", defenseName="Block", specialName="Hybernate", health = 40):
        self.__name = name
        self.__description = description
        self.__basicName = basicName
        self.__defenseName = defenseName
        self.__specialName = specialName
        self.__health = health
    def __str__(self):
        return self.__name

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def basicAttack(self, enemy):
        enemy.doDamage(10)

    def basicName(self):
        return self.__basicName

    def defenseAttack(self, enemy):
        self.doDamage(-10)

    def defenseName(self):
        return self.__defenseName

    def specialAttack(self, enemy):
        self.resetHealth()
    
    def specialName(self):
        return self.__specialName
    
    def getHealth(self):
        return self.__health
    
    def doDamage(self, damage):
        self.__health -= damage
    
    def resetHealth(self):
        self.__health = 40

class lapras(monster):
    def __init__(self, name="Lapras", description="A water type pokemon", basicName="Blizzard Burn", defenseName="Block", specialName="Ice Beam", health = 190):
        self.__name = name
        self.__description = description
        self.__basicName = basicName
        self.__defenseName = defenseName
        self.__specialName = specialName
        self.__health = health
    
    def __str__(self):
        return str(self.__name)
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description

    def basicAttack(self, enemy):
        enemy.doDamage(160)

    def basicName(self):
        return self.__basicName

    def defenseAttack(self, enemy):
        self.doDamage(-10)

    def defenseName(self):
        return self.__defenseName

    def specialAttack(self, enemy):
        enemy.doDamage(100)
        self.resetHealth()

    def specialName(self):
        return self.__specialName

    def getHealth(self):
        return self.__health

    def doDamage(self, damage):
        self.__health -= damage

    def resetHealth(self):
        self.__health = 160


class pile(monster):

    def __init__(self, name='Pile of Sh*t', description='It\'s a literal pile of sh*t', basicName='Splatter', defenseName='Steam', specialName='Waft', health=45):
        self.__name = name
        self.__description = description
        self.__basicName = basicName
        self.__defenseName = defenseName
        self.__specialName = specialName
        self.__health = health

    def __str__(self):
        return str(self.__name)

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def basicAttack(self, enemy):
        enemy.doDamage(10)

    def basicName(self):
        return self.__basicName

    def defenseAttack(self, enemy):
        self.doDamage(-10)

    def defenseName(self):
        return self.__defenseName

    def specialAttack(self, enemy):
        enemy.doDamage(20)

    def specialName(self):
        return self.__specialName

    def getHealth(self):
        return self.__health

    def doDamage(self, damage):
        self.__health -= damage

    def resetHealth(self):
        self.__health = 45


class tree(monster):

    def __init__(self, name='Oaker', description='Make like a Tree and have a kid with an Ogre.', basicName='Willow Womp', defenseName='Re-Root', specialName='Photosynthesis', health=200):
        self.__name = name
        self.__description = description
        self.__basicName = basicName
        self.__defenseName = defenseName
        self.__specialName = specialName
        self.__health = health

    def __str__(self):
        return str(self.__name)

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def basicAttack(self, enemy):
        enemy.doDamage(40)

    def basicName(self):
        return self.__basicName

    def defenseAttack(self, enemy):
        self.doDamage(-40)

    def defenseName(self):
        return self.__defenseName

    def specialAttack(self, enemy):
        self.resetHealth

    def specialName(self):
        return self.__specialName

    def getHealth(self):
        return self.__health

    def doDamage(self, damage):
        self.__health -= damage

    def resetHealth(self):
        self.__health = 200
