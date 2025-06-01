from .util import *
from .ray import Ray

class RayCast:
	def __init__(self, rays=[], angle=0, origin=(0,0)):
		self.rays = []
		self.angle = 0
		self.origin = np.array((0,0))
		self.outputs = []
		self.deltas = []
		self.ang_deltas = []

		for i in range(len(rays)):
			self.add_ray(rays[i])

		self.set_origin(origin)
		self.set_angle(angle)

	def add_ray(self, ray):
		self.rays.append(ray)
		self.deltas.append(ray.origin - self.origin)
		self.ang_deltas.append(ray.angle - self.angle)
		self.outputs.append(0)
	
	def set_origin(self, origin):
		self.origin = np.array(origin)
		for i in range(len(self.rays)):
			self.rays[i].set_origin(self.origin + self.deltas[i])

	def set_angle(self, angle):
		self.angle = cycle(angle, -np.pi, np.pi)
		for i in range(len(self.rays)):
			self.rays[i].set_angle(self.angle + self.ang_deltas[i])

	def rotate(self, delta):
		self.angle = cycle(self.angle + delta, -np.pi, np.pi)
		for i in range(len(self.rays)):
			self.rays[i].rotate(delta)

	def move(self, delta):
		# self.origin += np.array(delta)
		for i in range(len(self.rays)):
			self.rays[i].move(delta)

	def update(self, lines):
		for i in range(len(self.rays)):
			self.outputs[i] = self.rays[i].update(lines)
		return self.outputs		