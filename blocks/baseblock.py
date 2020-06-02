import pygame
from carconnection import *

WHITE = (255,255,255)
FONT = pygame.font.SysFont('Arial', 50)

class BaseBlock():
	#derived classes must define xpos and ypos
	def __init__(self, screen, connection, xpos, ypos):
		self.screen = screen
		self.connection = connection
		self.x = xpos
		self.y = ypos
		self.xsize = 0
		self.ysize = 0


	def click(self):
		return ""
	def update(self):
		pass
	def render(self):
		pass
	def cursorInside(self, x, y):
		if (self.x <= x and self.y <= y and self.x+self.xsize >= x and self.y+self.ysize >= y):
			return True
		return False