from .util import *

class Shape:
	def __init__(self, points=[], color=(255,255,255), linewidth=0):
		self.points=Vector(points)
		for i in range(len(self.points)):
			self.points[i]=P2Vector(self.points[i])
		self.polygon=Polygon([Point(*self.points[i]) for i in range(len(self.points))])
		self.linewidth=linewidth
		self.color=color

	def centroid(self):
		centroid=P2Vector()
		for point in self.points:
			centroid=centroid+P2Vector(point)/len(self.points)
		return centroid

	def rect(self):
		xmin,xmax,ymin,ymax=[None]*4
		for point in self.points:
			x,y=point
			if xmin==None or x<xmin: xmin=x
			if xmax==None or x>xmax: xmax=x
			if ymin==None or y<ymin: ymin=y
			if ymax==None or y>ymax: ymax=y
		return pygame.Rect(xmin, ymin, xmax-xmin, ymax-ymin)

	def draw(self, screen):
		pygame.draw.polygon(screen, self.color, self.points, self.linewidth)

	def transform(self, offset=[0,0], rotation=0, factor=1, center=None):
		if center is None:center=self.centroid()
		for i in range(len(self.points)):
			point=P2Vector(self.points[i])
			angle=translate_angle(compute_angle(center, point)+rotation)
			distance=compute_distance(center, point)*factor
			point=compute_position(center, distance, angle)
			self.points[i]=P2Vector(point)+P2Vector(offset)
		self.polygon=Polygon([Point(*self.points[i]) for i in range(len(self.points))])

	def translate(self, offset):
		self.transform(offset=offset)

	def rotate(self, rotation, center=None):
		self.transform(rotation=rotation, center=center)

	def scale(self, factor, center=None):
		self.transform(factor=factor, center=center)

	def copy(self, points=None, color=None, linewidth=None):
		points=self.points if points==None else points
		color=self.color if color==None else color
		linewidth=self.linewidth if linewidth==None else linewidth
		shape=Shape(points, color, linewidth)
		return shape

	def contains(self, point):
		return Point(*point).within(self.polygon)

	def json(self):
		data={
			"points":list([list(p) for p in self.points]),
			"color":list(self.color),
			"linewidth":self.linewidth}
		return data

	def save(self, filename):
		json.dump(self.json(), open(filename, 'w'))

	def load(self, filename):
		data=json.load(open(filename, 'r'))
		points=data['points']
		color=data['color']
		linewidth=data['linewidth']
		super().__init__(points, color, linewidth)
		return self
