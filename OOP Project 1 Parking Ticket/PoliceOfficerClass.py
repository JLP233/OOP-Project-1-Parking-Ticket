class PoliceOfficerClass:
    "Police officer who issues tickets."

def __init__(self, name: str, badge_number: str):
    self.name = name
    self.badge_number = badge_number

def __str__(self) -> str:
    return f"Officer {self.name} (Badge {self.badge_number})"