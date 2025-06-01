from .utilities import *

class GameManager:
	def __init__(self, screen_size):
		self.screen_size = np.array(screen_size, dtype=int)
		self.screen = pygame.display.set_mode(self.screen_size, pygame.SWSURFACE)
		self.running = True
		self.clock = pygame.time.Clock()
		self.dt = 0

		self.initialize()

	def initialize(self):
		pass

	def check_event(self, event):
		pass

	def update(self):
		pass

	def run(self):
		while self.running:
			self.dt = self.clock.tick() / 1000

			for event in pygame.event.get():
				self.check_event(event)

				if event.type == pygame.QUIT:
					self.running = False

			self.screen.fill((0,0,0))

			self.update()

			pygame.display.flip()
