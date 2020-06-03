from .baseblock import *
from carconnection import *


class ThrottleBar(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.value = "0"
		self.scaling = 2.0

	def click(self):
		return "throttle"
	def update(self):
		self.value = self.connection.getValue("throttle")
		pass
	def render(self):
		super().render()
		# draw a rectangle
		#pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)
		percentage = int(self.value)

		height = self.scaling*percentage #scaling purposes only


		pygame.draw.rect(self.screen, (0+(255/100*percentage),255-(255/100*percentage),0), pygame.Rect(self.x+50, self.y+100-height, 50, height))
		font1 = pygame.font.SysFont('Arial', 50)
		text = font1.render("Throttle %", False, (255,255,255))
		self.screen.blit(text,(self.x,self.y + self.scaling*55))

