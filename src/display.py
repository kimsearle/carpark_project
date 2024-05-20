class Display:

    def __init__(self, disp_id="", message="", is_on=False, car_park=None):
        self.disp_id = disp_id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"{self.disp_id}: {self.message}"

    def update(self, data):
        if "message" in data:
            self.message = data["message"]
