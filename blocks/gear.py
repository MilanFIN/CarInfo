from .baseblock import *
from carconnection import *


class Gear(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.value = ""

	def click(self):
		return ""
	def update(self):
		gear = self.connection.getValue("gear")
		self.value = gear

		pass
	def render(self):
		super().render()
		# draw a rectangle
		#pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)

		font1 = pygame.font.SysFont('Arial', 90)
		text = font1.render(self.value, False, (255,255,255))
		self.screen.blit(text,(self.x + 70,self.y + 160))
		font2 = pygame.font.SysFont('Arial', 70)
		text2 = font2.render("Gear", False, (255,255,255))
		self.screen.blit(text2,(self.x ,self.y + 230))
