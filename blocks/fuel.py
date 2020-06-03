from .baseblock import *
from carconnection import *


class Fuel(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.value = ""

	def click(self):
		return "fuelview"
	def update(self):
		pass
	def render(self):
		super().render()
		# draw a rectangle
		pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)

		font = pygame.font.SysFont('Arial', 75)

		text2 = font.render("Fuel", False, (255,255,255))

		self.screen.blit(text2,(self.x + 40,self.y + 95))