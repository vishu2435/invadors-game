from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from random import randint,random
from dock import Dock


class Fleet(GridLayout):
	survivors=ListProperty(())
	def __init__(self,**kw):
		super().__init__(**kw)
		for x in range(0,32):
			dock=Dock()
			self.add_widget(dock)
			self.survivors.append(dock)	
		self.center_x=Window.width/4
	def start_attack(self,instance,value):
		self.invasion.remove_widget(value)
		self.go_left(instance,value)
		self.schedule_events()

	def go_left(self,instance,value):
		print('Go_left Value is ',value)
		print('Go_left Instance is ',instance)
		
		animation=Animation(x=0)
		animation.bind(on_complete=self.go_right)
		animation.start(self)
	def go_right(self,instance,value):
		print('Go_right Value is ',value)
		print('Go_right Instance is ',instance)
		animation=Animation(right=self.parent.width)
		animation.bind(on_compelete=self.go_left)
		animation.start(self)
	def schedule_events(self):
		Clock.schedule_interval(self.solo_attack,1)
		Clock.schedule_once(self.shoot,random())
	def solo_attack(self,dt):
		if len(self.survivors):
			rint=randint(0,len(self.survivors)-1)
			child=self.survivors[rint]
			child.invader.drop_missile()
	def shoot(self,dt):
		if len(self.survivors):
			rint=randint(0,len(self.survivors)-1)
			child=self.survivors[rint]
			child.invader.drop_missile()
			Clock.schedule_once(self.shoot,random())
	def collide_ammo(self,ammo):
		for child in self.survivors:
			if child.invader.collide_widget(ammo):
				child.canvas.clear()
				self.survivors.remove(child)
				return True
		return False
	def on_survivors(self,instance,value):
		if len(self.survivors)==0:
			Clock.unschedule(self.solo_attack)
			Clock.unschedule(self.shoot)
			self.invasion.end_game("you win!")			