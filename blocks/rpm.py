from .baseblock import *
from carconnection import *


class Rpm(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.value = ""

	def click(self):
		return "rpm"
	def update(self):
		self.value = self.connection.getValue("rpm")
		pass
	def render(self):
		super().render()
		# draw a rectangle
		pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)


		text = FONT.render(self.value, False, (255,255,255))
		text2 = FONT.render("RPM", False, (255,255,255))

		self.screen.blit(text,(self.x + 45,self.y + 45))
		self.screen.blit(text2,(self.x + 45,self.y + 95))