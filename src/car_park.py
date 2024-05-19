from sensor import Sensor
from display import Display

class Car_park:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.sensors = sensors or []
        self.plates = plates or []
        self.displays = displays or []


    def __str__(self):
        return f'Car park at {self.location}, with {self.capacity} bays'


    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError('Object must be of type Sensor or Display')
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)



