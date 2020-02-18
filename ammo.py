from kivy.animation import Animation
from kivy.uix.image import Image
from boom import Boom

class Ammo(Image):
	def shoot(self,tx,ty,target):
		self.target=target
		self.animation=Animation(x=tx,top=ty)
		self.animation.bind(on_start=self.start)
		self.animation.bind(on_progress=self.progress)
		self.animation.bind(on_complete=self.stop)
		self.animation.start(self)
	def start(self,instance,value):
		print('Ammo parent',self.parent)
		self.boom=Boom()
		self.boom.center=self.center
		self.parent.add_widget(self.boom)
	def progress(self,instance,value,progression):
		print('progress',progression)
		if progression>=0.1:
			self.parent.remove_widget(self.boom)
		print('collide_ammo',self.target.collide_ammo(self))
		if self.target.collide_ammo(self):
			self.animation.stop(self)

	def stop(self,instance,value):
		self.parent.remove_widget(self)


class Shot(Ammo):
	pass

class Missile(Ammo):
	pass	