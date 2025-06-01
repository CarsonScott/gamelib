from .util import *

class Grid(dict):
	def __init__(self, cell_size=[1,1], neighborhood_size=[1,1]):
		self.cell_size=cell_size
		self.neighborhood_size=neighborhood_size

	def __setitem__(self, index, value):
		index=tuple(int(x) for x in index)
		super().__setitem__(index, value)

	def __getitem__(self, index):
		index=tuple(int(x) for x in index)
		return super().__getitem__(index)

	def get_index(self, position):
		index=tuple(math.floor(x) for x in P2Vector(position)/self.cell_size)
		return index

	def get_position(self, index):
		position=P2Vector(index)*self.cell_size
		return position

	def get_neighbors(self, index):
		i,j=index
		neighbors=[]
		w,h=self.neighborhood_size
		for x in range(i-math.floor(w/2), i+math.ceil(w/2)):
			for y in range(j-math.floor(h/2), j+math.ceil(h/2)):
				if (x,y)!=(i,j) and (x,y) in self:
					neighbors.append((x,y))
		return neighbors