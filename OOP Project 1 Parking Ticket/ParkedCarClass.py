class ParkedCarClass:
    "Identifying info for parked car."

def __init__(self, make: str, model: str, color: str, license_number: str, minutes_parked: int = 60):
    self.make = make
    self.model = model
    self.color = color
    self.license_number = license_number
    self.minutes_parked = minutes_parked

@property
def minutes_parked(self) -> int:
    return self._minutes_parked

@minutes_parked.setter
def minutes_parked(self, minutes: int) -> None:
        if not isinstance(minutes, int):
            raise TypeError("minutes_parked must be a whole number")
        if minutes <= 0:
            raise ValueError("minutes_parked cannot be less than 0")
        self._minutes_parked = minutes

def __str__(self) -> str:
    return f"{self.color} {self.make} {self.model} ({self.license_number}), parked {self.minutes_parked} min"