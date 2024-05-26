# tests/test_sensor.py
import unittest
from src.carpark import CarPark
from src.sensor import EntrySensor, ExitSensor


class TestEntrySensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor("E1", car_park=self.car_park)
        self.car_park.register(self.entry_sensor)

    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.car_park, self.car_park)

    def test_detect_vehicle_adds_car(self):
        initial_bay_count = self.car_park.available_bays
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), 1)
        self.assertEqual(self.car_park.available_bays, initial_bay_count - 1)


class TestExitSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor("E1", car_park=self.car_park)
        self.exit_sensor = ExitSensor("E2", car_park=self.car_park)
        self.car_park.register(self.entry_sensor)
        self.car_park.register(self.exit_sensor)
        # Add a car to the car park to be able to remove it
        self.entry_sensor.detect_vehicle()

    def test_exit_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.car_park, self.car_park)

    def test_detect_vehicle_removes_car(self):
        initial_bay_count = self.car_park.available_bays
        self.exit_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), 0)
        self.assertEqual(self.car_park.available_bays, initial_bay_count + 1)


if __name__ == "__main__":
    unittest.main()
