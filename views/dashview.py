from .baseview import *
from carconnection import *
from blocks.testblock import *
from blocks.rpm import *
from blocks.gear import *
from blocks.blank import *
from blocks.speed import *
from blocks.backbutton import *

class DashView(BaseView):
	def __init__(self, screen, connection):
		super().__init__(screen, connection)

		self.blocks.append(BackButton(screen, connection, 0,0))


		self.blocks.append(Speed(screen, connection, 95,43))
		self.blocks.append(Rpm(screen, connection, 313,80))
		self.blocks.append(Gear(screen, connection, 531,43))


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
	