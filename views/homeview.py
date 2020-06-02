from .baseview import *
from carconnection import *
from blocks.testblock import *
from blocks.rpm import *
from blocks.temperature import *

class HomeView(BaseView):
	def __init__(self, screen, connection):
		super().__init__(screen, connection)

		self.blocks.append(TestBlock(screen, connection, 95,43))
		self.blocks.append(Rpm(screen, connection, 313,43))
		self.blocks.append(TestBlock(screen, connection, 531,43))
		self.blocks.append(TestBlock(screen, connection, 95,261))
		self.blocks.append(Temperature(screen, connection, 313,261))
		self.blocks.append(TestBlock(screen, connection, 531,261))

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
