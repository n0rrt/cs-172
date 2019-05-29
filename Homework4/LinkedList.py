#Tim Harris tlh339 - LinkedList class
from Node import Node
class LinkedList:
    #from class notes
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return self.__head == None

    def append(self, data):
        newNode = Node(data)

        if self.isEmpty():
            self.__head = newNode
        else:
            current = self.__head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)

    def remove(self, item):
        current = self.__head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found == True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def __len__(self):
        if self.__head == None:
            return 0
        current = self.__head
        counter = 1
        while current.getNext() != None:
            counter += 1
            current = current.getNext()
        return counter
    def __str__(self):
        string = ""
        current = self.__head
        while current != None:
            string += str(current.getData()) + '->'
            current = current.getNext()
        return string
    def __getitem__(self, index):
        current = self.__head
        for i in range(index):
            current = current.getNext()
        return current.getData()