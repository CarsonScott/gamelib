class Device:
	def __init__(self):
		self.pressed=[]
		self.down=[]
		self.up=[]

	def is_pressed(self, button):
		return button in self.pressed

	def is_down(self, button):
		return button in self.down

	def is_up(self, button):
		return button in self.up

	def check_event(self, event):
		pass