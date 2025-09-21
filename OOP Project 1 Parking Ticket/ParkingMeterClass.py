class ParkingMeterClass:
    "Purhcased time from parking Meter."

def __init__(self, minutes_purchased: int = 60):
        self.minutes_purchased = minutes_purchased

@property
def minutes_purchased(self) -> int:
        return self._minutes_purchased