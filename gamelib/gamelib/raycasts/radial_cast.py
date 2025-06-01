from .util import *
from .ray import Ray
from .ray_cast import RayCast

class RadialCast(RayCast):
	def __init__(self, ray_count, length, angle_range=(-np.pi, np.pi), angle=0, origin=(0,0)):
		rays = []
		for i in range(ray_count):
			delta = (angle_range[1] - angle_range[0]) * i / ray_count
			angle = angle_range[0] + delta
			rays.append(Ray(length=length, angle=angle, origin=origin)) 
		super().__init__(rays=rays, angle=angle, origin=origin)