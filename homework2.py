from media import *


song1 = Song("song", "Waiting Room", "*****", "Fugazi", "13 Songs")
song2 = Song("song", "HEAT", "*****", "BROCKHAMPTON", "SATURATION")
song3 = Song("song", "Alright","*****", "Kendrick Lamar", "To Pimp A Butterfly")
song4 = Song("song", "Bound 2","*****", "Kanye West", "Yeezus")

movie1 = Movie("movie", "Pulp Fiction", "8.9/10", "Quentin Tarantino", "2 hours 34 minutes")
movie2 = Movie("movie", "The Matrix", "8.7/10", "The Wachowski Brothers", "2 hours 16 minutes")
movie3 = Movie("movie", "Inglorious Basterds", "8.3/10", "Quentin Tarantino", "2 hours 33 minutes")
movie4 = Movie("movie", "Spirited Away", "8.6/10", "Hayao Miyazaki", "2 hours 5 minutes")

picture1 = Picture("picture", "Mountain", "****", "1920x1080")
picture2 = Picture("picture", "Lake", "****", "1920x1080")
picture3 = Picture("picture", "Tree", "*****", "1920x1080")
picture4 = Picture("picture", "Dog", "*****", "1920x1080")

mediaList = [song1, song2, song3, song4, movie1, movie2, movie3, movie4, picture1, picture2, picture3, picture4]

def displayAll():
    for i in mediaList:
        (i.getAll())
        print("\n")
        
def displaySongs():
    for i in mediaList:
        if isinstance(i, Song):
            (i.getAll())
            print("\n")
def displayMovies():
    for i in mediaList:
        if isinstance(i, Movie):
            (i.getAll())
            print("\n")
def displayPictures():
    for i in mediaList:
        if isinstance(i, Picture):
            (i.getAll())
            print("\n")

if __name__ == "__main__":
    inMedia = False
    try:
        userIn = input("What do you want to display?\n")
    except:
        print("Enter valid input")
    while not(userIn.lower()==("quit")):
        if userIn.lower()==("display all"):
            displayAll()
        elif userIn.lower()==("display songs"):
            displaySongs()
        elif userIn.lower()==("display movies"):
            displayMovies()
        elif userIn.lower()==("display pictures"):
            displayPictures()
       
        elif userIn.lower().split()[0] == "play":
            for i in range(len(mediaList)):
                try:
                    if (str(userIn.lower().split()[1] + " " + userIn.lower().split()[2])) in mediaList[i].getName().lower():
                        mediaList[i].play()
                        inMedia = True
                        break
                except IndexError:
                    if (str(userIn.lower().split()[1]) in mediaList[i].getName().lower()):
                            mediaList[i].play()
                            inMedia=True
                            break
            if inMedia == False:
                print("Unable to find the requested media")
            inMedia = False

        else:
            inMedia = False
            for i in range(len(mediaList)):
                if userIn.lower()==(mediaList[i].getName().lower()):
                    mediaList[i].getAll()
                    inMedia = True
                    break
            if inMedia == False:
                print("Unable to find the requested media or command")
        userIn = input("What do you want to display?\n")
        inMedia = False   
