from monster import *

class bear(monster):   
    def __init__(self, name, description, basicName, defenseName, specialName, health):
        self.__name = "8 F***ing bears"
        self.__description = "They're 8 bears"
        self.__basicName = "Claw"
        self.__defenseName = "Block"
        self.__specialName = "Hybernate"
        self.__health = 40
    def __str__(self):
        return "8 big ol' bears"

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