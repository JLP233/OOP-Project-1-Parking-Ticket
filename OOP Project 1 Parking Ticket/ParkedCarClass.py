class ParkedCarClass:
    "Identifying info for parked car."

def __init__(self, make: str, model: str, color: str, license_number: str, minutes_parked: int = 60):
    self.make = make
    self.model = model
    self.color = color
    self.license_number = license_number
    self.minutes_parked = minutes_parked

