from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty

from screens import *

class Manager(ScreenManager):


    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)
        self.screen_one = ScreenOne()
        self.screen_two = ScreenTwo()
        self.screen_three = ScreenThree()
        self.screen_sail = Sail()
        self.screen_shotgun = Shotgun()
        self.screen_bluetooth = Bluetooth()
        self.screen_sensors1 = Sensors1()
        self.screen_glitter = Glitter()
        self.add_widget(self.screen_one)
        self.add_widget(self.screen_two)
        self.add_widget(self.screen_three)
        self.add_widget(self.screen_sail)
        self.add_widget(self.screen_shotgun)
        self.add_widget(self.screen_bluetooth)
        self.add_widget(self.screen_sensors1)
        self.add_widget(self.screen.glitter)
