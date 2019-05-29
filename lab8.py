from BST import *
import random
import matplotlib.pyplot as plt
import time


def populate(n):
    myList = []
    myBST = BST()
    while len(myList) != n:
        randNum = (random.randrange(0, n + 1))
        myList.append(randNum)
        myBST.append(randNum)
    return (myList, myBST)

def isIn(myList, num):
    for x in myList:
        if x == num:
            return True
    return False

def timing(myList, myBST):
    listTime1 = time.time()
    for val in myList:
        isIn(myList, val)
    listTime2 = time.time()
    listTimeFinal = listTime2 - listTime1
    bstTime1 = time.time()
    for val in myList:
        myBST.isin(val)
    bstTime2 = time.time()
    bstTimeFinal = bstTime2 - bstTime1
    return (listTimeFinal, bstTimeFinal)
    print("List time: {}\nBST time: {}".format(listTimeFinal, bstTimeFinal))
if __name__ == "__main__":
    tup=populate(100)
    newList=tup[0]
    newBST=tup[1]
    count=0
    for val in newList:
        if isIn(newList, val):
            count += 1
    print(count)
    bstTimes = []
    listTimes = []
    xVals = []
    for n in range(1, 10000, 1000):
        newTup = populate(n)
        newList = newTup[0]
        newBST = newTup[1]
        times = timing(newList, newBST)
        listTime = times[0]
        bstTime = times[1]
        listTimes.append(listTime)
        bstTimes.append(bstTime)
        xVals.append(n)
    plt.plot(xVals, listTimes, label="List times")
    plt.plot(xVals, bstTimes, label="BST times")
    plt.legend()
    plt.show()