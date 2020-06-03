from .baseblock import *
from carconnection import *


class Fuelpercentage(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.value = ""
		self.scaling = 2.0

	def click(self):
		return "fuelview"
	def update(self):
		self.value = self.connection.getValue("fuelpercentage")
		pass
	def render(self):
		super().render()
		# draw a rectangle
		#pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)
		percentage = int(self.value)
		height = self.scaling*percentage #scaling purposes only
		pygame.draw.rect(self.screen, (255-(255/100*percentage),0+(255/100*percentage),0), pygame.Rect(self.x, self.y+150-height, 50, height))



		font1 = pygame.font.SysFont('Arial', 100)
		font2 = pygame.font.SysFont('Arial', 80)

		text = font1.render(self.value+"%", False, (255,255,255))
		text2 = font2.render("Fuel left", False, (255,255,255))

		self.screen.blit(text,(self.x + 60,self.y + 80))
		self.screen.blit(text2,(self.x + 5,self.y + 160))