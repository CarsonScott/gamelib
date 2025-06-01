from .util import *

class Ray:
	def __init__(self, length, angle=0, origin=(0,0)):
		self.length = length
		self.angle = angle
		self.origin = np.array(origin)
		self.output = 0
		self.line = None

	def set_origin(self, origin):
		self.origin = np.array(origin)

	def set_angle(self, angle):
		self.angle = cycle(angle, -np.pi, np.pi)

	def rotate(self, delta):
		self.angle = cycle(self.angle + delta, -np.pi, np.pi)

	def move(self, delta):
		self.origin = self.origin + np.array(delta)

	def update(self, lines):
		self.line = project_line(self.origin, self.angle, self.length)

		max_length = self.length
		for line in lines:
			position = line_intersection(self.line, line)
			if position is not None:
				distance = np.linalg.norm(self.origin - position)
				if distance < max_length:
					max_length = distance
					self.line[1] = position

		self.output = 1 - max_length / self.length
		return self.output