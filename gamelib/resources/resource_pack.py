from .util import *
from .resource import Resource 

class ResourcePack(dict):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.properties={}
		self.load_resources()

	def load(self, filename):
		self.__init__(json.load(open(filename, 'r')))
		return self

	def save(self, filename):
		data=dict(self)
		data['properties']=self.properties
		json.dump(data, open(filename, 'w'))

	def load_resources(self):
		for i in self:
			if self[i]['type']=='surface':
				filename=self[i]['filename']
				properties=self[i].properties
				self[i]=load_image(filename)
				self.properties[i]=properties
	
			elif self[i]['type']=='spritesheet':
				kernel=self[i]['kernel']
				filename=self[i]['filename']
				surfaces=parse_spritesheet(load_image(filename), pygame.Rect(0,0,*kernel))
				keys=list(self[i].properties.keys())
				self.properties[i]=self[i].properties
				self[i]={}
				for j in range(len(keys)):
					self[i][keys[j]]=surfaces[j]
		return self

	def get(self, key):
		if ':' in key:
			key=key.split(':')
			obj=self
			for i in key:
				obj=obj[i]
			return obj
		else:return self[key]

	def get_properties(self, key):
		if ':' in key:
			key=key.split(':')
			obj=self.properties
			for i in key:
				obj=obj[i]
			return obj
		else:return self.properties[key]