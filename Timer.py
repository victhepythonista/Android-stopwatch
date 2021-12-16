import sys
import time
import random
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from  kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.logger import Logger
from kivy.clock import Clock
from  kivy.graphics import Line , Canvas , Color ,Rectangle
from kivy.uix.screenmanager import Screen,ScreenManager


from backend import GetWidgetRoot,AddWidgets,PrettifyTime
BASE =  [round(.01*i, 2) for i in range(7,10)]
COLORS  = [(random. choice(BASE), random. choice(BASE), random. choice(BASE), 1) for i in range(226)] 
def  AppConfiguration():
	# screen configurations...size,resizable
	print("configuring screen")
	Config.set('graphics', 'resizable',False)
	Config.set('graphics', 'borderless',True)
	Config.set('kivy', 'exit_on_escape', '0')
	#Window.size= 340,600
	Window.clearcolor = (0.13,0.13,.14, 1)

AppConfiguration()

class OptionsButton(Button):
	'''
opens a dropdown menu with
[exit]  and  [help] buttons
	'''
	pass

class ControlButton(Button):

    pass

class AppTitle(Label):
    'text = Timer app..self exp.'


    pass
class Rect(Label):
	'''
	 as imple line ..just pass in the coordinates when intializing
	  and voila
	'''
	def __init__(self,pos, size,**kwargs ):
		Label.__init__(kwargs)
		self.coordinates = coordinates
		color = .4,.5,.6,.9
		with self.canvas :
			Rectangle(size = size, pos = pos)
			Color(color)



class TimerLabel(Label):
	def __init__(self,**kwargs):
		Label.__init__(self)
		self.anchor_time = 0
		self.now_time = 0
		self.raw_time = 0
		self.tick_time = .1
		self.paused = False
		self.paused_time = 0
		self.time_wasted = 0
		self.stopped = False
		
	def AlternateBackground(self, interval ):
		random_color = random.choice(COLORS)
		self. ChangeColor(random_color)
	def RunCount(self, interval ):
		self.UpdateAll()
	def UpdateAll(self):
		if   self.paused == False:
			self.UpdateTime()
			self.UpdateText()
			return
		self.time_wasted = time.time()  - self.paused_time
	def UpdateText(self):
		self.text  = PrettifyTime(self.raw_time)
	def UpdateTime(self):


		self.raw_time = time.time() - self.anchor_time
	def EndCount(self):
		Clock.unschedule(self.RunCount)
		Clock.unschedule(self. AlternateBackground) 

	def StartCount(self):
		Clock.unschedule(self.RunCount)
		Clock.schedule_interval(self.RunCount, self.tick_time)
		
		Clock.unschedule(self. AlternateBackground)
		Clock. schedule_interval(self.AlternateBackground,1)

	def Start(self):
		self.stopped = False
		self.paused = False
		## start the timer ....reset also
		self.anchor_time = time.time()
		self.UpdateAll()
		self.StartCount()
	def Stop(self):
		# stop  the timer
		self.EndCount()
		self.stopped = True
	def Pause(self):
		# pause the timer

		self.paused = True
		self.paused_time = time.time()
		self.EndCount()
	def Resume(self):
		# resume counting

		self.anchor_time = self.paused_time - self.raw_time
		self.paused = False
		self.StartCount()
	def PauseOrResume(self):
		if not self.stopped:
			if self.paused:
				self.Resume()
				return
			self.Pause()

	def Reset(self):
		# reset the timer but do not start
		Clock.unschedule(self.RunCount)
		self.text = "00:00:00"
	def ChangeColor(self, color):
		with self. canvas. before:
			Color(rgba = color)
			Rectangle(size=self. size, pos = self. pos)


class HomeScreenContainer(FloatLayout):

	def on_kv_post(self, instance):
		print(f'This is ROOT : {self.parent.parent}')



class HomeScreen(Screen):
    pass
class RootWidget(ScreenManager):
    pass
class TimerApp(App):
    pass


if __name__  == '__main__':
    TimerApp().run()
