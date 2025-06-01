from .utilities import *

class Camera(pygame.Surface):
	def __init__(self, size, position=P2Vector()):
		super().__init__(size)
		self.position=position

	def get_rect(self):
		return pygame.Rect(self.position, super().get_rect().size)


	def blit(self, source, dest, area=None, special_flags=0):
		if isinstance(dest, pygame.Rect):
			dest=dest.topleft
		dx,dy=self.position
		x,y=dest
		dest=(x-dx,y-dy)
		super().blit(source, dest, area, special_flags)

	def set_center(self, position):
		x,y=position
		w,h=self.get_rect().size
		x-=w/2
		y-=h/2
		self.position=P2Vector(x,y)

	def get_center(self):
		x,y=self.position
		w,h=self.get_rect().size
		return P2Vector(x+w/2, y+h/2)

	