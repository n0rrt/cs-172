#Tim Harris tlh339 - Node class
class Node:
    #from class notes
    def __init__(self, data, next = None):
        self.__data = data
        self.__next = next
    def getData(self):
        return self.__data
    def getNext(self):
        return self.__next
    def setData(self, newData):
        self.__data = newData
    def setNext(self, newNext):
        self.__next = newNext
    def __str__(self):
        return str(self.__data, self.__next)