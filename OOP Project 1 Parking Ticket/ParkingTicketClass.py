import math

class ParkingTicketClass:
    "Ticket issued for cars parked over alotted time."

def __init__(self, car, officer, overtime_minutes: int):
    if not isinstance(overtime_minutes, int):
        raise TypeError("overtime_minutes must be a whole number")
    if overtime_minutes <= 0:
        raise ValueError("overtime_minutes must be greater than 0")
    self.car = car
    self.officer_name = officer.name
    self.badge_number = officer.badge_number
    self.overtime_minutes = overtime_minutes
    self.fine = self.calculate_fine()

def calculate_fine(self) -> float:
    hours = math.ceil(self.overtime_minutes / 60)
    if hours <= 0:
        return 0.0
    return 25.0 + 10.0 * (hours - 1)

