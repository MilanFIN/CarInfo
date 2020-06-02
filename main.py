import os
import time
import pygame


pygame.init()
pygame.font.init()

# views
from views.baseview import *
from views.testview import *
from views.homeview import *
from views.rpmview import *
from carconnection import *


WIDTH = 800
HEIGHT = 480

class CarInfo():
	def __init__(self):
		self.views = {}
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption('vectra')

		self.connection = CarConnection()

		self.views["test"] = TestView(self.screen, self.connection)
		self.views["home"] = HomeView(self.screen, self.connection)
		self.views["rpm"] = RpmView(self.screen, self.connection)

		self.activeView = "home"

	def run(self):
		pass
		while (True):
			events = pygame.event.get()
			for event in events:
				if (event.type == pygame.MOUSEBUTTONUP):
					if (event.button == 1): # left mouse
						x, y = pygame.mouse.get_pos()
						nextView = self.views[self.activeView].click(x, y)
						if (nextView != ""):
							self.activeView = nextView

				elif (event.type == pygame.QUIT):
					return


			self.views[self.activeView].update()
			self.views[self.activeView].render()
			pygame.display.flip()

			self.clock.tick(60)

def main():

	car = CarInfo()
	car.run()



if __name__ == '__main__':
	main()