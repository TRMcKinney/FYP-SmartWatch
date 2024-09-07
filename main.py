import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
os.environ['KIVY_AUDIO'] = 'sdl2'
#os.environ['KIVY_WINDOW'] = 'sdl2'
#os.environ['KIVY_TEXT'] = 'sdl2'


from kivy.app import App
from kivy.properties import ListProperty, NumericProperty
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

from subprocess import call


from screenmanager import Manager
# Using a * imports everything from the file
from screens import *
from misc_widgets import ClockButton
from arduinothread import ArduinoThread

dir = os.path.join('.', 'kv')
for file in os.listdir(dir):
    print(file)
    Builder.load_file('./kv/' + file)

class ScreensApp(App):


    sensorList = ListProperty()
    sensor1 = NumericProperty(0)
    sensor2 = NumericProperty(0)
    sensor3 = NumericProperty(0)
    sensor4 = NumericProperty(0)
    sensor5 = NumericProperty(0)

    def __init__(self, **kwargs):
        super(ScreensApp, self).__init__(**kwargs)
        # Initialise the class and create a self.sound variable.
        self.manager = Manager()
        self.sound = None
        self.keepThread = True
        self.arduino = ArduinoThread(self, True)
        self.arduino.start()
        Clock.schedule_interval(self.extensiongesture, 1)
        Clock.schedule_interval(self.flexiongesture, 1)
        Clock.schedule_interval(self.ulnargesture, 1)
        Clock.schedule_interval(self.radialgesture, 1)

    def on_sensorList(self, instance, value):
        if value[0]:
            self.sensor1 = value[0]
        if len(value) > 1:
            self.sensor2 = value[1]
            self.sensor3 = value[2]
            self.sensor4 = value[3]
            self.sensor5 = value[4]

    def extensiongesture(self,dt):
        if self.manager.current == 'Sensors1':
            if self.sensor1 > 200 and self.sensor2 > 70 and self.sensor3 > 15 and self.sensor5 > 90:
                self.play_sound('sail.wav')
                print("Extension Gesture")

    def flexiongesture(self,dt):
        if self.manager.current == 'Sensors1':
            if self.sensor1 > 95 and self.sensor2 > 25 and self.sensor3 > 100:
                self.stop_sound()
                print("Flexion Gesture")
                
    def ulnargesture(self,dt):
        if self.manager.current == 'Sensors1':
            if self.sensor2 > 35 and self.sensor3 > 40 and self.sensor5 > 40:
                self.play_sound('shotgun.wav')
                print("Ulnar Deviation Gesture")

    def radialgesture(self,dt):
        if self.manager.current == 'Sensors1':
            if self.sensor1 > 240 and self.sensor2 > 70 and self.sensor3 > 10:
                self.play_sound('glitter.wav')
                print("Radial Deviation Gesture")
        

#    def on_sensor2(self, instance, value):
#        print("New sensor 2 value: " + str(value))
        

#    def on_sensor3(self, instance, value):
#        print("New sensor 3 value: " + str(value))

    def play_sound(self, sound_file):
        """Pass the 'sound_file' path from the on_release function of the button that plays the sound"""
        if not self.sound:
            print("Playing Sound")
            self.sound = SoundLoader().load(sound_file)
            self.sound.play()

    def stop_sound(self):
        """Check if self.sound exists to not cause any crashes and then stop it playing the sound"""
        if self.sound:
            print("Stopping sound")
            self.sound.stop()
            self.sound = None

    def build(self):
        return self.manager

    def on_stop(self):
        self.keepThread = False
        self.arduino.breakBool = False
        
    def poweroff(self):
        call("sudo shutdown -h now", shell=True)

if __name__ == "__main__":
    try:
        app = ScreensApp()
        app.run()
    except KeyboardInterrupt:
        app.arduino.breakBool = False
