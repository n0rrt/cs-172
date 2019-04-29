class Media:
    def __init__(self, media_type, name, rating):
        self.__media_type = media_type
        self.__name = name
        self.__rating = rating
    def __str__(self):
        return str(self.__media_type, self.__name, self.__rating)
    def getType(self):
        return self.__media_type
    def getName(self):
        return self.__name
    def getRating(self):
        return self.__rating
class Movie(Media):
    def __init__(self, media_type, name, rating, director, runtime):
        self.__director = director
        self.__runtime = runtime
        super().__init__(self)

    def __str__(self):
        return str(self.__media_type, self.__name, self.__rating, self.__director, self.__runtime)
   
    def play(self):
        print("{}, playing now".format(self.__name))

    def getDirector(self):
        return self.__director
    
    def getRuntime(self):
        return self.__runtime

class Song(Media):
    def __init__(self, media_type, name, rating, artist, album):
        self.__artist = artist
        self.__album = album
        super().__init__(self)
    def __str__(self):
        return str(self.__media_type, self.__name, self.__rating, self.__artist, self.__album)
    
    def play(self):
        print("{} by {}, now playing".format(self.__name, self.__artist))

    def getArtist(self):
        return self.__artist
    def getAlbum(self):
        return self.__album
class Picture(Media):
    def __init__(self, media_type, name, rating, resolution):
        self.__resolution = resolution
        super().__init__(self)
    
    def __str__(self):
        return str(self.__media_type, self.__name, self.__rating, self.__resolution)
    
    def show(self):
        print("Showing {}".format(self.__name))
    
    def getResolution(self):
        return self.__resolution

