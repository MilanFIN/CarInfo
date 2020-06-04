from .baseblock import *
from carconnection import *


class Rpm(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.value = ""
		self.maxHeight = 200
		self.maxValue = 8000 # the max rpm in the car

	def click(self):
		return ""
	def update(self):
		self.value = self.connection.getValue("rpm")
		pass
	def render(self):
		super().render()
		# draw a rectangle

		rpm = int(self.value)

		if (rpm > self.maxValue):
			rpm = self.maxValue

		scaling = self.maxHeight/self.maxValue		

		height = scaling*rpm #scaling purposes only
		fraction = rpm / self.maxValue

		pygame.draw.rect(self.screen, (0+(255*fraction),255-(255*fraction),0), pygame.Rect(self.x, self.y+200, 50, -height))
		font1 = pygame.font.SysFont('Arial', 60)
		text = font1.render(self.value, False, (255,255,255))
		self.screen.blit(text,(self.x + 70,self.y + 160))
		font2 = pygame.font.SysFont('Arial', 70)
		text2 = font2.render("RPM", False, (255,255,255))
		self.screen.blit(text2,(self.x ,self.y + 230))





