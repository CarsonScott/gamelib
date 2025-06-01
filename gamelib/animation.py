from .utilities import *

class Animation:
	def __init__(self, frames, frame_rate):
		if not all_equal([frame.get_rect().size for frame in frames]):
			raise Exception('Frames must be the same size.')
		self.duration = len(frames) * frame_rate
		self.frame_rate = frame_rate
		self.frames = frames
		self.timer = 0
		self.index = 0

	def update(self, dt):
		self.timer = cycle(self.timer + dt, 0, self.duration)
		self.index = int(np.floor(len(self.frames) * self.timer / self.duration))
		return self.frames[self.index]
