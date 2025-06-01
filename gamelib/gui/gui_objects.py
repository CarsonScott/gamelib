from .util import *

class GUIObject:
	def __init__(self, size=(1,1), position=(0,0)):
		self.size = np.array(size)
		self.position = np.array(position)

	@property
	def rect(self):
		return pygame.Rect(self.position, self.size)

	def check_event(self, event):
		pass

	def draw(self, screen):
		pass

	def update(self):
		pass

	def reset(self):
		pass

class Button(GUIObject):

	def __init__(self, size, position=(0,0)):
		super().__init__(size=size, position=position)
		self.onclick = 0
		self.onrelease = 0
		self.active = 0

	def check_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				mouse = pygame.mouse.get_pos()
				if self.rect.collidepoint(mouse):
					self.onclick = 1
					self.active = 1
		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				if self.active == 1:
					self.onrelease = 1
					self.active = 0

	def reset(self):
		if self.onclick == 1:
			self.onclick = 0

	def draw(self, screen):
		if self.active:
			color = [255, 255, 255]
			border = [255, 255, 255]
		else: 
			color = [0, 0, 0]
			border = [50, 50, 50]
		rect = self.rect
		pygame.draw.rect(screen, color, rect)
		pygame.draw.rect(screen, border, rect, 1)

class Switch(GUIObject):

	def __init__(self, size, position=(0,0)):
		super().__init__(size=size, position=position)
		self.onclick = 0
		self.active = 0

	def check_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				mouse = pygame.mouse.get_pos()
				if self.rect.collidepoint(mouse):
					self.onclick = 1
					self.active = int(not self.active)

	def reset(self):
		if self.onclick == 1:
			self.onclick = 0

	def draw(self, screen):
		if self.active:
			color = [255, 255, 255]
			border = [255, 255, 255]
		else: 
			color = [0, 0, 0]
			border = [150, 150, 150]
		rect = self.rect
		pygame.draw.rect(screen, color, rect)
		pygame.draw.rect(screen, border, rect, 1)

class Slider(GUIObject):
	def __init__(self, size, position=(0,0)):
		super().__init__(size=size, position=position)
		self.onclick = 0
		self.onrelease = 0
		self.active = 0
		self.value = 0

	@property
	def slide_rect(self):
		left, top = self.position
		width, height = self.rect.size
		value = self.value
		w = height / 2
		h = height + 8
		x = (left - w / 2) + width * value
		y = top - 4
		return pygame.Rect(x, y, w, h)

	def check_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				mouse = pygame.mouse.get_pos()
				if self.slide_rect.collidepoint(mouse):
					self.onclick = 1
					self.active = 1
		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				if self.active == 1:
					self.onrelease = 1
					self.active = 0

	def update(self):
		if self.active:
			rect = self.rect
			slide_rect = self.slide_rect
			mouse = pygame.mouse.get_pos()
			x = clamp(mouse[0], rect.left, rect.right)
			self.value = (x - rect.left) / rect.width

	def reset(self):
		if self.onclick == 1:
			self.onclick = 0

	def draw(self, screen, offset=np.array((0,0))):
		rect = self.rect
		rect.topleft = np.array(rect.topleft)
		slide_rect = self.slide_rect
		color = [150, 150, 150]
		slide_color = [255, 255, 255]
		pygame.draw.rect(screen, color, rect, 1)
		pygame.draw.rect(screen, slide_color, slide_rect)

