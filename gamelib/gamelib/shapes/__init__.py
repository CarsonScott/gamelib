from .shape import Shape 
from .shape_group import ShapeGroup

def Rectangle(center, size, color=(255,255,255), linewidth=0):
	w,h=size
	x,y=center
	x-=w/2
	y-=h/2
	points=[
		[x,y],
		[x+w,y],
		[x+w,y+h],
		[x,y+h]]
	return Shape(points, color, linewidth)

def Equilateral(center, base, color=(255,255,255), linewidth=0):
	points=[
		compute_position(center, base/2, -90*math.pi/180),
		compute_position(center, base/2, 30*math.pi/180),
		compute_position(center, base/2, 150*math.pi/180)
	]
	return Shape(points, color, linewidth)

def Normal(center, sides, length, color=(255,255,255), linewidth=0):
	a=0
	da=2*math.pi/sides
	points=[]
	for i in range(sides):
		p=compute_position(center, length, a)
		points.append(p)
		a+=da
	return Shape(points, color, linewidth)