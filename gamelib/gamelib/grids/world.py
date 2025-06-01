from .util import *
from .grid import Grid

class World(Grid):
	def __init__(self, cell_size, chunk_shape, neighborhood_size):
		super().__init__(cell_size*chunk_shape, neighborhood_size)
		self.chunk_shape=P2Vector(chunk_shape)
		self.loaded={}

	def add_chunk(self, index, chunk):
		self[index]=Grid(self.cell_size/self.chunk_shape)
		for i in range(len(chunk)):
			for j in range(len(chunk[i])):
				self[index][(j,i)]=chunk[i][j]

	def get_position(self, index):
		i,j=index
		if isinstance(i, tuple) and isinstance(j, tuple):
			return self.get_position(i)+self[i].get_position(j)
		else:return super().get_position(index)

	def load_chunk(self, index):
		if index in self and index not in self.loaded:
			self.loaded[index]=[]
			chunk=self[index]
			position=self.get_position(index)
			for i in chunk:
				resource_id=chunk[i]
				rect=pygame.Rect(position+self[index].get_position(i), chunk.cell_size)
				self.loaded[index].append((resource_id, rect))

	def unload_chunk(self, index):
		if index in self and index in self.loaded:
			del self.loaded[index]

	def get_loaded(self):
		loaded=concatenate(*list(self.loaded.values()))
		return loaded

	def update(self, position):
		index=self.get_index(position)
		neighbors=self.get_neighbors(index)
		loaded=neighbors+[index]
		to_load=[]
		to_unload=[]
		for i in self.loaded:
			if i not in loaded:to_unload.append(i)
		for i in loaded:
			if i not in self.loaded:to_load.append(i)
		for i in to_unload:self.unload_chunk(i)
		for i in to_load:self.load_chunk(i)
		return self.get_loaded()

	def draw(self, screen, resource_pack):
		loaded=self.get_loaded()
		for i in range(len(loaded)):
			id,rect=loaded[i]
			screen.blit(resource_pack.get(id), rect)
