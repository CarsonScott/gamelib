from .device import Device 
from .util import *

class Mouse(Device):
	def check_event(self, event):
		if event.type==pygame.MOUSEBUTTONDOWN:
			button=event.button
			self.down.append(button)
			self.pressed.append(button)
		elif event.type==pygame.MOUSEBUTTONUP:
			button=event.button
			self.up.append(button)
			if button in self.pressed:
				self.pressed.remove(button)