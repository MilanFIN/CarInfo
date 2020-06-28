import os
import time
import pygame


pygame.init()
pygame.font.init()

# views
from views.baseview import *
from views.testview import *
from views.homeview import *
from views.dashview import *
from views.engineview import *
from views.fuelview import *
from views.drivingview import *
from carconnection import *
from litersper100 import *

WIDTH = 800
HEIGHT = 480

class CarInfo():
	def __init__(self):
		self.views = {}
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption('vectra')

		self.connection = CarConnection()
		self.litersPer100 = LitersPer100()

		self.views["testview"] = TestView(self.screen, self.connection)
		self.views["homeview"] = HomeView(self.screen, self.connection)
		self.views["dashview"] = DashView(self.screen, self.connection)
		self.views["engineview"] = EngineView(self.screen, self.connection)
		self.views["fuelview"] = FuelView(self.screen, self.connection, self.litersPer100)
		self.views["drivingview"] = DrivingView(self.screen, self.connection)

		self.activeView = "homeview"


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


			#update liters/100km
			self.litersPer100.setSpeed(float(self.connection.getValue("speed")))
			self.litersPer100.setFuel(float(self.connection.getValue("fuelpercentage")))



			self.views[self.activeView].update()
			self.views[self.activeView].render()
			pygame.display.flip()

			self.clock.tick(60)
			


def main():

	car = CarInfo()
	car.run()



if __name__ == '__main__':
	main()