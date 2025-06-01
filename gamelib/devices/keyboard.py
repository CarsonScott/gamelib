from .device import Device
from ..utilities import *

class Keyboard(Device):
	def check_event(self, event):
		if event.type==pygame.KEYDOWN:
			key=event.key
			self.down.append(key)
			self.pressed.append(key)
		elif event.type==pygame.KEYUP:
			key=event.key
			self.up.append(key)
			if key in self.pressed:
				self.pressed.remove(key)