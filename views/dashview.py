from .baseview import *
from carconnection import *
from blocks.testblock import *
from blocks.rpm import *
from blocks.gear import *
from blocks.blank import *
from blocks.speed import *
from blocks.backbutton import *
from blocks.throttlebar import *

class DashView(BaseView):
	def __init__(self, screen, connection):
		super().__init__(screen, connection)

		self.blocks.append(BackButton(screen, connection, 0,0))


		self.blocks.append(Speed(screen, connection, 150,80))
		self.blocks.append(Rpm(screen, connection, 360,80))
		self.blocks.append(ThrottleBar(screen, connection, 580,190))


	def click(self, x, y):
		nextView = ""
		for block in self.blocks:
			if (block.cursorInside(x, y)):
				nextView = block.click()
				break
		return nextView
	def update(self):
		super().update()
	def render(self):
		super().render()
		for block in self.blocks:
			block.render()
	