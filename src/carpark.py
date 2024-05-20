from src.sensor import Sensor
from src.display import Display


class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.sensors = sensors or []
        self.plates = plates or []
        self.displays = displays or []

    def __str__(self):
        return f'Car park at {self.location}, with {self.capacity} bays'

    @property
    def available_bays(self):
        if len(self.plates) < self.capacity:
            return self.capacity - len(self.plates)
        else:
            return 0

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError('Object must be of type Sensor or Display')
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)

