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
        super().__init__
    def __str__(self, self.__media_type, self.__name, self.__rating, self.__director, self.__runtime):
        return str(self.__media_type, self.__name, self.__rating, self.__director, self.__runtime)
    def play(self):
        print("{}, playing now".format(self.__name))
    
