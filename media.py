class Media:
    def __init__(self, media_type, name, rating):
        self.__media_type = media_type
        self.__name = name
        self.__rating = rating
    def __str__(self):
        return str(self.getType(), self.getName(), self.getRating())
    def getType(self):
        return self.__media_type
    def getName(self):
        return self.__name
    def getRating(self):
        return self.__rating
    def getAll(self):
        print(self)
            
class Movie(Media):
    def __init__(self, media_type, name, rating, director, runtime):
        self.__director = director
        self.__runtime = runtime
        super().__init__(media_type, name, rating)

    def __str__(self):
        return self.getName() + "\n" + self.getDirector() + "\n" + self.getRating()
   
    def play(self):
        print("{}, playing now".format(self.getName()))

    def getDirector(self):
        return self.__director
    
    def getRuntime(self):
        return self.__runtime

class Song(Media):
    def __init__(self, media_type, name, rating, artist, album):
        self.__artist = artist
        self.__album = album
        super().__init__(media_type, name, rating)
    def __str__(self):
        return self.getName() + "\n" + self.getArtist() + "\n" + self.getAlbum() + "\n" + self.getRating()
    
    def play(self):
        print("{} by {}, now playing".format(self.getName(), self.getArtist()))

    def getArtist(self):
        return self.__artist
    def getAlbum(self):
        return self.__album
class Picture(Media):
    def __init__(self, media_type, name, rating, resolution):
        self.__resolution = resolution
        super().__init__(media_type, name, rating)
    
    def __str__(self):
        return self.getName() + "\n" + self.getResolution() + "\n" + self.getRating()

    def play(self):
        print("Showing {}".format(str(self.getName())))
    
    def getResolution(self):
        return self.__resolution
