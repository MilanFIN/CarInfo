from .baseblock import *
from carconnection import *


class SteeringBar(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.value = "0"
		self.scaling = 1.5

	def click(self):
		return "throttle"
	def update(self):
		self.value = self.connection.getValue("steering")
		pass
	def render(self):
		super().render()
		# draw a rectangle
		#pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)
		angle = int(self.value)

		width = self.scaling*angle #scaling purposes only


		pygame.draw.rect(self.screen, (0+(255/100*abs(angle)),255-(255/100*abs(angle)),0), pygame.Rect(self.x+self.scaling*75, self.y+50, width, 50))
		font1 = pygame.font.SysFont('Arial', 50)
		text = font1.render("Steering angle", False, (255,255,255))
		self.screen.blit(text,(self.x,self.y+110))

