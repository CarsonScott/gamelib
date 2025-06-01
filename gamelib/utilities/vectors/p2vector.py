from .vector import Vector

class P2Vector(Vector):
	def __init__(self, *args, value=0):
		if len(args)==0:args=[value]*2
		super().__init__(*args, value=value, params={'x':0, 'y':1})
