from .util import *

class Sprite(pygame.sprite.Sprite):

	@property
	def image(self):
		return rotate_center(self.original, math.degrees(-self.angle))

	@property
	def rect(self):
		rect=self.image.get_rect()
		rect.center=self.position
		return rect

	def __init__(self, image, position=P2Vector(), angle=0):
		super().__init__()
		self.angle=angle
		self.original=image
		self.position=position

	def rotate(self, delta):
		self.angle=translate_angle(self.angle+delta)

	def translate(self, delta):
		self.position=P2Vector(self.position)+P2Vector(delta)

	def draw(self, screen):
		screen.blit(self.image, self.rect)

	def update(self, *args, **kwargs):
		pass