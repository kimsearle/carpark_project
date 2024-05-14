class Sensor:
    def __init__(self, sensor_id, is_active=False, car_park=""):
        self.sensor_id = sensor_id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor: {self.sensor_id}, is active: {self.is_active}"


class EntrySensor(Sensor):
    pass


class ExitSensor(Sensor):
    pass

