from gamelib import *
from database import *

game=Game((640,480))

class FourierTransform(Network):
	def __init__(self, origin):
		super().__init__(node=Template(origin=None, length=0, angle=0, position=P2Vector()))
		self.origin=origin

	def add_node(self, length, angle):
		if len(self.get_instances('node')) > 0:
			origin=self.get_instances('node')[len(self.get_instances('node'))-1]
		self.object('node', key, origin=origin, length=length, angle=angle)