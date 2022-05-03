import time
import multiprocessing
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pynput import keyboard
from pygame import mixer
import keyboard



class Flashlight(object):
    """Flashlight"""

    def __init__(self):
        self.initiate = int(time.time())
        self.on = 0
        self.off = 1
        self.shine = False  # Off when initiating
        self.life = 0
        self.battery = 20 - self.life

    def __str__(self):
        return f'Flashlight status [{"on" if self.shine else "off"}] Battery: {self.battery}'

    def recharge(self):
        self.battery = 100

    def _music(self):
        mixer.init()
        mixer.music.load('sample3.wav')
        mixer.music.play()
        time.sleep(1)

    def _regulator(self):
        self.shine = True
        p = multiprocessing.Process(target=self._music(), args=())
        p.start()
        print(f'Flashlight on.')
        self.on = int(time.time())
        keyboard.wait('space')
        self.off = int(time.time())
        self.life = self.off - self.on
        self.battery = self.battery - self.life
        mixer.music.stop()
        p.terminate()
        print(f'Flashlight off. Battery left: {self.battery}')
        self.shine = False

    def click(self):
        if self.battery > 0:
            self._regulator()
        else:
            print('Flashlight is out of battery')




f = Flashlight()

def start():
    print('ON - [q], OFF - [space], Recharge battery [r], EXIT - [Esc]. [b] is buggy')
    while True:
        if f.shine == False:
            if keyboard.is_pressed('q'):
                f.click()
            if keyboard.is_pressed('r'):
                f.recharge()
            if keyboard.is_pressed('b'):
                print(f.battery)    # printing lot of times. WHY????????
            if keyboard.is_pressed('esc'):
                print('Have a nice day!')
                break


if __name__ == '__main__':
    start()
