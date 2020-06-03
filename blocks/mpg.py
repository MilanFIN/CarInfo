from .baseblock import *
from carconnection import *


class Mpg(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.speed = ""


	def click(self):
		return "lper100"
	def update(self):
		self.value = self.connection.getValue("speed")
		pass
	def render(self):
		super().render()
		# draw a rectangle
		#pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)

		font1 = pygame.font.SysFont('Arial', 100)
		font2 = pygame.font.SysFont('Arial', 80)

		text = font1.render("?", False, (255,255,255))
		text2 = font2.render("L/100", False, (255,255,255))

		self.screen.blit(text,(self.x + 40,self.y + 30))
		self.screen.blit(text2,(self.x + 40,self.y + 95))