from .resource import Resource 
from .resource_pack import ResourcePack

def surface_resource(filename):
		return super().__init__('surface', filename)

def spritesheet_resource(filename, kernel, properties={}):
		resource=Resource(type='spritesheet', filename=filename, kernel=kernel, properties=properties)
		return resource

