from .baseblock import *
from carconnection import *


class Blank(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.value = ""

	def click(self):
		return ""
	def update(self):
		pass
	def render(self):
		super().render()
		# draw a rectangle
		pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)
