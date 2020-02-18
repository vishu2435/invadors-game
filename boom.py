from kivy.uix.image import Image
from kivy.core.audio import SoundLoader

class Boom(Image):
	sound=SoundLoader.load('boom.wav')
	def boom(self,**kw):
		self.__class__.sound.play()
		super().__init__(**kw)