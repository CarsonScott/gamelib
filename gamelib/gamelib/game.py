from .camera import Camera 
from .manager import Manager 
from .utilities import *

class Game:
	def __init__(self, screen_size):
		self.screen_size=screen_size
		self.manager=None
		self.camera=None
		self.running=True
		self.dt=0

	def run(self):
		self.manager=Manager()
		self.camera=Camera(self.screen_size)
		screen=pygame.display.set_mode(self.screen_size)
		while self.running:
			for event in pygame.event.get():
				self.manager.check_event(event)
				if event.type==pygame.QUIT:
					self.running=False
			screen.fill((0,0,0))
			self.camera.fill((0,0,0))
			self.update()
			self.draw()
			screen.blit(self.camera, (0,0))
			pygame.display.flip()
		pygame.quit()

	def initialize(self, *args, **kwargs):
		pass

	def update(self):
		pass

	def draw(self):
		pass