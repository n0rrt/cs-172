#Tim Harris tlh339 - Employee class
class Employee:
    def __init__(self, idNum, rate, hours=0, wages=0):
        self.__idNum = idNum
        self.__hours = hours
        self.__rate = rate
        self.__wages = wages
    
    #setters
    def setId(self, newId):
        self.__idNum = newId
    def setHours(self, newHours):
        self.__hours = newHours
    def setRate(self, newRate):
        self.__rate = newRate
    def setWage(self, newWage):
        self.__wages = newWage
    
    #getters
    def getId(self):
        return self.__idNum
    def getHours(self):
        return self.__hours
    def getRate(self):
        return self.__rate
    def getWage(self):
        return self.__wages
    
    def __str__(self):
        return str(self.__idNum) + " " + str(self.__hours) + " " + str(self.__rate) + " " + str(self.__wages)
    
