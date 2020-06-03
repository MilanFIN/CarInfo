from .baseblock import *
from carconnection import *


class Speed(BaseBlock):
	def __init__(self, screen, connection, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 175

		self.value = ""

	def click(self):
		return ""
	def update(self):
		speed = self.connection.getValue("speed")
		self.value = speed

		pass
	def render(self):
		super().render()
		# draw a rectangle
		pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)


		text = FONT.render(self.value, False, (255,255,255))
		text2 = FONT.render("km/h", False, (255,255,255))

		self.screen.blit(text,(self.x + 45,self.y + 45))
		self.screen.blit(text2,(self.x + 45,self.y + 95))