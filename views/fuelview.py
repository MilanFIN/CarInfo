from .baseview import *
from carconnection import *
from litersper100 import *
from blocks.blank import *
from blocks.backbutton import *
from blocks.fuelpercentage import *
from blocks.mpg import *
from blocks.range import *
from blocks.resetmpg import *

class FuelView(BaseView):
	def __init__(self, screen, connection, litersper100):
		super().__init__(screen, connection)

		self.blocks.append(BackButton(screen, connection, 0,0))

		self.blocks.append(Fuelpercentage(screen, connection, 50,150))

		self.blocks.append(Mpg(screen, connection, litersper100, 300,150))
		
		self.blocks.append(Range(screen, connection, litersper100, 550,150))

		self.blocks.append(ResetMpg(screen, connection, litersper100, 330, 350))

		#self.blocks.append(Blank(screen, connection, 95,43))
		#self.blocks.append(Blank(screen, connection, 313,43))
		#self.blocks.append(Blank(screen, connection, 531,43))
		#self.blocks.append(Blank(screen, connection, 95,261))
		#self.blocks.append(Blank(screen, connection, 313,261))
		#self.blocks.append(Blank(screen, connection, 531,261))


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
	