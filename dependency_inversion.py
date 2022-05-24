from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("Light Bulb is on")

    def turn_off(self):
        print("Light Bulb is off")

class Fan(Switchable):
    def turn_on(self):
        print("Fan is on")

    def turn_off(self):
        print("Fan is off")

class ElectricPowerSwitch:
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
        else:
            self.client.turn_on()
        self.on = not self.on

l = LightBulb()
f = Fan()
switch = ElectricPowerSwitch(l)
switch.press()
print(switch.on)
switch.press()
print(switch.on)
switch.press()
print(switch.on)