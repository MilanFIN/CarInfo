from .baseview import *
from carconnection import *
from blocks.testblock import *
from blocks.backbutton import *

class TestView(BaseView):
	def __init__(self, screen, connection):
		super().__init__(screen, connection)

		self.blocks.append(BackButton(screen, connection, 0,0))
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
	