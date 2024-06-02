from src.carpark import CarPark
from src.sensor import EntrySensor, ExitSensor
from src.display import Display

car_park = CarPark(location="Moondalup", capacity=100, log_file="moondalup.txt")

entry_sensor = EntrySensor(sensor_id=1, is_active=True, car_park=car_park)
exit_sensor = ExitSensor(sensor_id=2, is_active=True, car_park=car_park)
display = Display(disp_id=1, message="Welcome to Moondalup", is_on=True, car_park=car_park)

car_park.register(entry_sensor)
car_park.register(exit_sensor)
car_park.register(display)

for i in range(10):
    entry_sensor.detect_vehicle()

for i in range(2):
    exit_sensor.detect_vehicle()

print(f"Final available bays: {car_park.available_bays}")
print(f"Log file contents:")
with car_park.log_file.open() as f:
    print(f.read())