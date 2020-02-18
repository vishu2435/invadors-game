from kivy.uix.widget import Widget
from invaders import Invader

class Dock(Widget):
	def __init__(self,**kw):
		super().__init__(**kw)
		self.invader=Invader()
		self.add_widget(self.invader)
		self.bind_invader()
	def bind_invader(self,instance=None):
		self.invader.formation=True
		self.bind(pos=self.on_pos)
	def unbind_invader(self):
		self.invader.formation=False
		self.unbind(pos=self.on_pos)
	def on_pos(self,instance,value):
		self.invader.pos=self.pos