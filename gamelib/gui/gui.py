from .util import *

class GUI:
	def __init__(self, *objects):
		self.offset = np.array((0,0))
		self.objects = {}
		self.index = 0
		self.running = True
		for obj in objects:
			self.add(obj)

	def add(self, *obj):
		indices = []
		for o in obj:
			index = self.index
			self.objects[index] = o
			self.index += 1
			indices.append(index)
		if len(indices) == 1:
			return indices[0]
		return indices

	def remove(self, *indices):
		for i in np.flip(np.sort(indices)):
			del self.objects[i]

	def check_event(self, event):
		for i in self.objects:
			self.objects[i].check_event(event)

	def update(self):
		for i in self.objects:
			self.objects[i].update()

	def reset(self):
		for i in self.objects:
			self.objects[i].reset()

	def draw(self, screen):
		for i in self.objects:
			self.objects[i].draw(screen)

	def step(self, screen):
		self.reset()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			self.check_event(event)
		self.update()
		self.draw(screen)
		return self.running