from .util import *

class Vector(list):
	def __init__(self, *args, shape=None, value=0, params={}):
		self.params=params
		if len(args)==1 and (isinstance(args[0], list) or isinstance(args[0], tuple)):
			args=args[0]
		if shape!=None:
			shape=list(shape)
			args=[]
			for i in range(shape[0]):
				if len(shape)==1:
					args.append(value)
				else:args.append(Vector(shape=shape[1:], value=value))
		args=list(args)
		for i in range(len(args)):
			if isinstance(args[i], list) or isinstance(args[i], tuple):
				args[i]=Vector(*args[i])
		super().__init__(args)

	def __getattr__(self, key):
		if key=='params':
			return super().__getattr__(key)
		else:return self[self.params[key]]

	def __setattr__(self, key, value):
		if key=='params':
			super().__setattr__(key,value)
		else:self[self.params[key]]=value

	def convert_input(self, other):
		if not (isinstance(other, list) or isinstance(other, tuple)):
			other=Vector(shape=self.shape[len(self.shape)-1:], value=other)
		else:other=Vector(*other)
		index=None
		if other.shape!=self.shape:
			for i in range(len(self.shape)):
				if other.shape==self.shape[i:]:
					index=i
					break
		if index!=None:
			other=Vector(shape=self.shape[0:index], value=other)
		return other

	def __sub__(self, other):
		other=self.convert_input(other)
		if self.shape!=other.shape:raise InvalidShapeException(self, other)
		else:return type(self)([self[i]-other[i] for i in range(len(self))])

	def __add__(self, other):
		other=self.convert_input(other)
		if self.shape!=other.shape:raise InvalidShapeException(self, other)
		else:return type(self)([self[i]+other[i] for i in range(len(self))])

	def __mul__(self, other):
		other=self.convert_input(other)
		if self.shape!=other.shape:raise InvalidShapeException(self, other)
		else:return type(self)([self[i]*other[i] for i in range(len(self))])

	def __truediv__(self, other):
		other=self.convert_input(other)
		if self.shape!=other.shape:raise InvalidShapeException(self, other)
		else:return type(self)([self[i]/other[i] for i in range(len(self))])

	def __lt__(self, other):
		other=self.convert_input(other)
		if self.shape!=other.shape:raise InvalidShapeException(self, other)
		else:return all([self[i] < other[i] for i in range(len(self))])		

	def __gt__(self, other):
		other=self.convert_input(other)
		if self.shape!=other.shape:raise InvalidShapeException(self, other)
		else:return all([self[i] > other[i] for i in range(len(self))])

	def __eq__(self, other):
		other=self.convert_input(other)
		if self.shape!=other.shape:raise InvalidShapeException(self, other)
		else:return all([self[i] == other[i] for i in range(len(self))])

	def __le__(self, other):
		other=self.convert_input(other)
		if self.shape!=other.shape:raise InvalidShapeException(self, other)
		else:return all([self[i] <= other[i] for i in range(len(self))])

	def __ge__(self, other):
		other=self.convert_input(other)
		if self.shape!=other.shape:raise InvalidShapeException(self, other)
		else:return all([self[i] >= other[i] for i in range(len(self))])

	def __str__(self, indent=0, spacing='\t'):
		embedded=False
		strings=[]
		for i in range(len(self)):
			if isinstance(self[i], Vector):
				embedded=True
				string=self[i].__str__(indent+1, spacing)
			else:string=str(self[i])
			strings.append(string)
		string='['
		for i in range(len(strings)):
			si=strings[i]
			if embedded:
				string+='\n'+spacing*(indent+1)+si
				if i==len(strings)-1:
					string+='\n'+spacing*indent+']'
				else:string+=', '
			else:
				string+=si
				if i==len(strings)-1:
					string+=']'
				else:string+=', '
		return string

	@property
	def shape(self):
		shape=[len(self)]
		if len(self) > 0:
			if not isinstance(self[0], Vector):
				if isinstance(self[0], list) or isinstance(self[0], tuple):
					self[0]=Vector(self[0])
			if isinstance(self[0], Vector):
				shape+=list(self[0].shape)
		return tuple(shape)


