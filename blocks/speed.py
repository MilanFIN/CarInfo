from .baseblock import *
from carconnection import *


class Speed(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.value = ""
		self.maxHeight = 200
		self.maxValue = 130 # max expected saturation value

	def click(self):
		return ""
	def update(self):
		speed = self.connection.getValue("speed")
		self.value = speed

		pass
	def render(self):
		super().render()
		# draw a rectangle
		speed = int(self.value)

		if (speed > self.maxValue):
			speed = self.maxValue

		scaling = self.maxHeight/self.maxValue		

		height = scaling*speed #scaling purposes only
		fraction = speed / self.maxValue

		pygame.draw.rect(self.screen, (0+(255*fraction),255-(255*fraction),0), pygame.Rect(self.x, self.y+200, 50, -height))
		font1 = pygame.font.SysFont('Arial', 60)
		text = font1.render(self.value, False, (255,255,255))
		self.screen.blit(text,(self.x + 70,self.y + 160))
		font2 = pygame.font.SysFont('Arial', 70)
		text2 = font2.render("km/h", False, (255,255,255))
		self.screen.blit(text2,(self.x ,self.y + 230))

