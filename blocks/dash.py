from .baseblock import *
from carconnection import *


class Dash(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.value = ""

	def click(self):
		return "dashview"
	def update(self):
		pass
	def render(self):
		super().render()
		# draw a rectangle
		pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)

		font = pygame.font.SysFont('Arial', 45)

		text2 = font.render("Dashboard", False, (255,255,255))

		self.screen.blit(text2,(self.x + 8,self.y + 95))