from .util import *
from .mover import Mover

class Agent(Mover):

	def __init__(self, accel_rate, deccel_rate, max_speed, image=DEFAULT_AGENT_IMAGE, position=P2Vector(), angle=0):
		super().__init__(image, position, angle)
		self.accel_rate=accel_rate
		self.deccel_rate=deccel_rate
		self.max_speed=max_speed

	def update_velocity(self, dt):
		angle=self.movement_angle()
		velocity=P2Vector(self.velocity)-P2Vector(math.cos(angle), math.sin(angle))*self.deccel_rate*dt
		if self.velocity.x!=0 and sign(velocity.x)!=sign(self.velocity.x):velocity.x=0
		if self.velocity.y!=0 and sign(velocity.y)!=sign(self.velocity.y):velocity.y=0
		self.velocity=velocity
		super().update_velocity(dt)

	def update_speed(self, dt):
		super().update_speed(dt)
		if self.speed > self.max_speed:
			angle=self.movement_angle()
			self.velocity=P2Vector(math.cos(angle), math.sin(angle))*self.max_speed*dt
			self.speed=self.max_speed