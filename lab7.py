from room import *
from maze import *

'''
0123456
SRRRRRR
7   8 9
R###R#R
10
R######
11/12
RR#####
 13/14
#RR####

3x south
1x east
1x south
1x east

'''
rooms = []
rooms.append(Room("This room is the entrance."))
rooms.append(Room("This room has a table. Maybe a dining room?"))
rooms.append(Room('This room has several toilets in a circle. Weird.'))
rooms.append(Room('This room is empty, save for a nickle on the floor. Neat!'))
rooms.append(Room('This room has a bookshelf. Perhaps it\'s a personal libary'))
rooms.append(Room('This room has a prehistoric computer lining the walls. How vintage.'))
rooms.append(Room('This room contains a squirrel. We\'re not quite sure why either.'))
rooms.append(Room('This room has a table with a key in the shape of a skull on top. It might not be useful in the future but God it looks cool.'))
rooms.append(Room('This room has another squirrel. Don\'t worry, it\'s not the same room.'))
rooms.append(Room('This room has a cash register and a few weapons on a table. Perhaps a shop? But where\'s the shopkeep...'))
rooms.append(Room('This room is very much different when compared to the others, much taller. It\'s still just an ordinary room, though.'))
rooms.append(Room('This room contains a squirrel-wedding ceremony. Perhaps the prevoius squirrels were ushers?'))
rooms.append(Room('This room is empty, no nickle this time. What was up with that squirrel wedding though?'))
rooms.append(Room('This room contains a heavy door with a skull on it. Now would be a great time for that-- oh it\'s already unlocked.'))
rooms.append(Room("This room is the exit. Good Job."))

start = rooms[0]

# top row of rooms
for x in range(6):
    rooms[x].setEast(rooms[x+1])
    rooms[x+1].setWest(rooms[x])

rooms[0].setSouth(rooms[7])
rooms[7].setNorth(rooms[0])

rooms[4].setSouth(rooms[8])
rooms[8].setNorth(rooms[4])

rooms[6].setSouth(rooms[9])
rooms[9].setNorth(rooms[6])

rooms[7].setSouth(rooms[10])
rooms[10].setNorth(rooms[7])

rooms[10].setSouth(rooms[11])
rooms[11].setNorth(rooms[10])

rooms[11].setEast(rooms[12])
rooms[12].setWest(rooms[11])

rooms[12].setSouth(rooms[13])
rooms[13].setNorth(rooms[12])

rooms[13].setSouth(rooms[14])
rooms[14].setNorth(rooms[13])

maze = Maze(rooms[0], rooms[14])

while True:
    print(maze.getCurrent())

    userIn = input("Enter direction to move north south east west restart\n")
    if userIn.lower() == 'north':
        if maze.moveNorth():
            print('You went north')
            maze.setCurrent(rooms[rooms.index(maze.getCurrent().getNorth())])
            if maze.atExit():
                print('You found the exit')
                break
            
        else:
            print("Direction invalid")
            
    elif userIn.lower() == 'south':
        if maze.moveSouth():
            print('You went south')
            maze.setCurrent(rooms[rooms.index(maze.getCurrent().getSouth())])
            if maze.atExit():
                print('You found the exit')
                break
            
        else:
            print('Direction invalid')
            
    elif userIn.lower() == 'east':
        if maze.moveEast():
            print('You went east')
            maze.setCurrent(rooms[rooms.index(maze.getCurrent().getEast())])
            if maze.atExit():
                print('You found the exit')
                break
            
        else:
            print('Direction invalid')
            
    elif userIn.lower() == 'west':
        if maze.moveWest():
            print('You went west')
            maze.setCurrent(rooms[rooms.index(maze.getCurrent().getWest())])
            if maze.atExit():
                print('You found the exit')
                break
           
        else:
            print('Direction invalid')
           
    elif userIn.lower() == 'restart':
        maze.reset()
    #debug
    elif userIn.lower() == 'index':
        print(rooms.index(maze.getCurrent()))
    else:
        print('invalid input try again')
    


