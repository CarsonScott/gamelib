from .util import *
from .sprite import Sprite

class Mover(Sprite):

	def __init__(self, image, position=P2Vector(), angle=0):
		super().__init__(image, position, angle)
		self.acceleration=P2Vector()
		self.velocity=P2Vector()
		self.collisons=[0,0,0,0]
		self.speed=0

	def movement_distance(self):
		return compute_norm(self.velocity)

	def movement_angle(self):
		return math.atan2(self.velocity.y, self.velocity.x)

	def apply_force(self, force, angle, dt):
		self.acceleration=P2Vector(self.acceleration)+P2Vector(math.cos(angle), math.sin(angle))*force*dt

	def update_speed(self, dt):
		self.speed=self.movement_distance()/dt

	def update_velocity(self, dt):
		self.velocity=P2Vector(self.velocity)+P2Vector(self.acceleration)

	def update_position(self, dt, rects=[]):
		self.acceleration=P2Vector()
		left,right,top,bottom=[0]*4
		self.position.x+=self.velocity.x*dt
		rect=self.rect
		for r in rects:
			if rect.colliderect(r):
				if self.velocity.x < 0:
					self.position.x = r.right + rect.width/2
					self.velocity.x = 0
					left = 1
				elif self.velocity.x > 0:
					self.position.x = r.left - rect.width/2
					self.velocity.x = 0
					right = 1
		self.position.y+=self.velocity.y*dt
		rect=self.rect
		for r in rects:
			if rect.colliderect(r):
				if self.velocity.y < 0:
					self.position.y = r.bottom + rect.height/2
					self.velocity.y = 0
					top = 1
				elif self.velocity.y > 0:
					self.position.y = r.top - rect.height/2
					self.velocity.y = 0
					bottom = 1
		self.collisions=[left,right,top,bottom]

	def update(self, dt, rects=[]):
		self.update_velocity(dt)
		self.update_speed(dt)
		self.update_position(dt, rects)
		self.acceleration=P2Vector()

	def compute(self, *args, **kwargs):
		pass