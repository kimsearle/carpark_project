import unittest
from src.display import Display
from src.carpark import CarPark


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.carpark = CarPark("The Moon", 100)
        self.display = Display(disp_id=1, message="Welcome to the carpark", is_on=True, car_park=self.carpark)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.disp_id, 1)
        self.assertEqual(self.display.message, "Welcome to the carpark")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")


if __name__ == "__main__":
    unittest.main()
