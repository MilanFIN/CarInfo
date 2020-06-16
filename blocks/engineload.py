from .baseblock import *
from carconnection import *


class EngineLoad(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.value = ""

	def click(self):
		return ""
	def update(self):
		gear = self.connection.getValue("engineload")
		self.value = gear

		pass
	def render(self):
		super().render()
		# draw a rectangle
		#pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)

		font1 = pygame.font.SysFont('Arial', 80)
		text = font1.render(self.value+"%", False, (255,255,255))
		self.screen.blit(text,(self.x + 20,self.y))
		font2 = pygame.font.SysFont('Arial', 55)
		text2 = font2.render("Engine", False, (255,255,255))
		text3 = font2.render("load", False, (255,255,255))

		self.screen.blit(text2,(self.x ,self.y + 70))
		self.screen.blit(text3,(self.x ,self.y + 105))
