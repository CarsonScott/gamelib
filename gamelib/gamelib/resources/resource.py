from .util import *

class Resource(dict):
	def __init__(self, type, filename, properties={}, **kwargs):
		self['type']=type
		self['filename']=filename
		for i in kwargs:self[i]=kwargs[i]
		self.properties=properties
