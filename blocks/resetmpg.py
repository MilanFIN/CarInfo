import time

from .baseblock import *
from carconnection import *
from litersper100 import *


class ResetMpg(BaseBlock):
	def __init__(self, screen, connection, litersper100, xpos, ypos):
		super().__init__(screen, connection, xpos, ypos)
		self.xsize = 175
		self.ysize = 82

		self.speed = ""
		self.litersper100 = litersper100

		self.lastClickTime = time.time()

		self.clickDelay = 1 #max time in between double click's

	def click(self):
		clickTime = time.time()
		if (clickTime - self.lastClickTime <= self.clickDelay):
			self.litersper100.reset()
		self.lastClickTime = clickTime
		return ""
	def update(self):
		pass
	def render(self):
		super().render()
		# draw a rectangle
		#pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)
		pygame.draw.rect(self.screen, WHITE, pygame.Rect(self.x, self.y, self.xsize, self.ysize), 3)

		font1 = pygame.font.SysFont('Arial', 40)
		text = font1.render("RESET", False, (255,255,255))

		self.screen.blit(text,(self.x + 20,self.y + 20))
