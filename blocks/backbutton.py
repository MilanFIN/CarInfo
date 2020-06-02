from .baseblock import *
from carconnection import *


class BackButton(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 80
		self.ysize = 50

	def click(self):
		return "homeview"
	def update(self):
		self.connection.getValue("test")
		pass
	def render(self):
		super().render()
		# draw a rectangle
		pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(self.x+2, self.y+2, self.xsize-2, self.ysize-2))
		pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)
		pygame.draw.line(self.screen, WHITE, (self.x + 25, self.y+10), (self.xsize-25, self.ysize-10), 3)
		pygame.draw.line(self.screen, WHITE, (self.x + 25, self.y+self.ysize-10), (self.xsize-25, self.y +10), 3)
