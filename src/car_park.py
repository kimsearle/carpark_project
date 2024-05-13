class Car_park:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.sensors = []
        self.plates = []
        self.displays = []


    def __str__(self):
        return f'Car_park({self.location}, {self.capacity})'

