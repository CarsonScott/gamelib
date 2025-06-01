from .vector import Vector

class P3Vector(Vector):
	def __init__(self, *args, value=0):
		if len(args)==0:args=[value]*3
		super().__init__(*args, value=value, params={'x':0, 'y':1, 'z':2})
