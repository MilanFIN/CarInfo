from .baseblock import *
from carconnection import *
from litersper100 import *


class Mpg(BaseBlock):
	def __init__(self, screen, connection, litersper100, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.speed = ""
		self.litersper100 = litersper100

	def click(self):
		return ""
	def update(self):
		pass
	def render(self):
		super().render()
		# draw a rectangle
		#pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)

		font1 = pygame.font.SysFont('Arial', 75)
		font2 = pygame.font.SysFont('Arial', 50)
		value = self.litersper100.getLitersPer100()
		value = f"{value:.2f}"
		text = font1.render(value, False, (255,255,255))
		text2 = font2.render("L/100", False, (255,255,255))

		self.screen.blit(text,(self.x + 40,self.y + 30))
		self.screen.blit(text2,(self.x + 40,self.y + 95))