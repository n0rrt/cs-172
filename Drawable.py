import pygame
import abc

class Drawable(metaclass = abc.ABCMeta):
	def __init__(self,x=0,y=0):
		self.__x=x
		self.__y=y
		
	def getLoc(self):
		return (self.__x, self.__y)
		
	def setLoc(self,p):
		self.__x = p[0]
		self.__y = p[1]
	
	
	@abc.abstractmethod
	def draw(self,surface):
		pass

class Rectangle(Drawable):
	def __init__(self, x=0, y=0, width=0, height=0, color=(0,0,0)):
		self.__width = width
		self.__height = height
		self.__color = color
		super().__init__(self, x, y)
	def draw(self, surface):
		pygame.draw.rectangle(surface, self.__color, (self.__x, self.__y), (self.__width, self.__height))