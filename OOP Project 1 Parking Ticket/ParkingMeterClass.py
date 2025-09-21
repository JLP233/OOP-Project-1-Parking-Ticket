class ParkingMeterClass:
    "Purchased time from parking Meter."

    def __init__(self, minutes_purchased: int = 60):
        self.minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self) -> int:
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, minutes: int) -> None:
        if not isinstance(minutes, int):
            raise TypeError("minutes_purchased must be a whole number")
        if minutes <= 0:
            raise ValueError("minutes_purchased cannot be less than 0")
        self._minutes_purchased = minutes

    def __str__(self) -> str:
        return f"Meter purchased: {self.minutes_purchased} min"