from .baseblock import *
from carconnection import *


class TestBlock(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

	def click(self):
		return "test"
	def update(self):
		self.connection.getValue("test")
		pass
	def render(self):
		super().render()
		# draw a rectangle
		pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)


		text = FONT.render('Text', False, (255,255,255))

		self.screen.blit(text,(self.x + 30,self.y + 30))