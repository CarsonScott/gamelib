from .vector import Vector

class Color(Vector):
	def __init__(self, *args, value=0):
		if len(args)==0:args=[value]*3
		if len(args)==1:args=[args[0]]*3
		if len(args)==3:args=tuple(list(args)+[255])
		super().__init__(*args, value=value, params={'r':0, 'g':1, 'b':2, 'a':3})

