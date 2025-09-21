from ParkedCarClass import ParkedCarClass
from ParkingMeterClass import ParkingMeterClass
from PoliceOfficerClass import PoliceOfficerClass

def run_and_print(car, meter, officer, title: str):
    print(f"\n {title}")
    print(f"Car: {car}")
    print(f"Meter: {meter}")
    print(f"Officer: {officer}")
    ticket = officer.inspect_car(car, meter)
    if ticket:
        print("Result: Ticket Issued \n" + str(ticket))
    else:
        print("Result: Ticket not issued / Car parked legally.")

def scenario_1():
    car = ParkedCarClass("Toyota", "Camry", "Red", "XYZ123", minutes_parked=30)
    meter = ParkingMeterClass(minutes_purchased=40)
    officer = PoliceOfficerClass("John Doe", "5678")
    run_and_print(car, meter, officer, "Scenario 1: Car Parked Legally")