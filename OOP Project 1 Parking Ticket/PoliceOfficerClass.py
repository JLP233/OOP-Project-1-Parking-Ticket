from ParkingTicketClass import ParkingTicketClass

class PoliceOfficerClass:
    "Police officer who issues tickets."

def __init__(self, name: str, badge_number: str):
    self.name = name
    self.badge_number = badge_number

def inspect_car(self, car, meter):
    "Return a parking ticket if the car is parked over the paid for time"
    overtime = car.minutes_parked - meter.minutes_purchased
    if overtime > 0:
        return ParkingTicketClass(car, self, overtime)

def __str__(self) -> str:
    return f"Officer {self.name} (Badge {self.badge_number})"

