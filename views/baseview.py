import pygame
from carconnection import *
from blocks import *

class BaseView():
	def __init__(self, screen, connection):
		self.screen = screen
		self.connection = connection
		self.blocks = []

	def click(self, x, y):
		pass
	def update(self):
		for block in self.blocks:
			block.update()
	def render(self):
		self.screen.fill((0, 0, 20))

	