from .util import *
from .grid import Grid

class Chunk(Grid):
	def __init__(self, cell_size):
		super().__init__(cell_size)