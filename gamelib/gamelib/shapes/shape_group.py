from .util import *

class ShapeGroup(list):
	def __init__(self, shapes=[]):
		super().__init__(shapes)

	@property
	def centroid(self):
		X=[self[i].centroid.x for i in range(len(self))]
		Y=[self[i].centroid.y for i in range(len(self))]
		x=sum(X)/len(X)
		y=sum(Y)/len(Y)
		return Point(x,y)

	@property
	def rect(self):
		xmin,xmax,ymin,ymax=[None,None,None,None]
		for shape in self:
			for point in shape.points:
				x,y=point
				if xmin==None:
					xmin,xmax=(x,x)
					ymin,ymax=(y,y)
				else:
					if x < xmin:xmin=x
					if x > xmax:xmax=x
					if y < ymin:ymin=y
					if y > ymax:ymax=y
		width=xmax-xmin
		height=ymax-ymin
		return pygame.Rect(xmin, ymin, width, height)

	def copy(self):
		group=ShapeGroup()
		for i in range(len(self)):
			group.append(self[i].copy())
		return group

	def rotate(self, rotation, center=None):
		if center is None:center=self.centroid
		for i in range(len(self)):
			self[i].rotate(rotation, center)

	def translate(self, offset):
		for i in range(len(self)):
			self[i].translate(offset)

	def transform(self, offset=[0,0], angle=0, scale=1, center=None):
		if center is not None:
			center=self.centroid
		group=self.copy()
		center=self.get_center() if center==None else center
		for i in range(len(group)):
			group[i]=group[i].transform(offset, angle, scale, center)
		return group

	def draw(self, surface):
		for i in range(len(self)):
			self[i].draw(surface)

	def contains(self, point):
		for i in range(len(self)):
			if self[i].contains(point):
				return True
		return False

	def within(self, point):
		for i in range(len(self)):
			if self[i].within(point):
				return True
		return False

	def json(self):
		data=[self[i].json() for i in range(len(self))]
		return data

	def save(self, filename):
		json.dump(self.json(), open(filename, 'w'))

	def load(self, filename):
		shapes=[]
		data=json.load(open(filename, 'r'))
		for i in range(len(data)):
			points=data[i]['points']
			color=data[i]['color']
			linewidth=data[i]['linewidth']
			shape=Shape(points, color, linewidth)
			shapes.append(shape)
		super().__init__(shapes)
		return self