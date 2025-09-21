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

def scenario_2():
    car = ParkedCarClass("Honda", "Accord", "Blue", "ABC987", minutes_parked=70)
    meter = ParkingMeterClass(minutes_purchased=60)
    officer = PoliceOfficerClass("Jane Smith", "1234")
    run_and_print(car, meter, officer, "Scenario 2: Car Illegally Parked Past Alotted Time by 10 Minutes")

def scenario_3():
    car = ParkedCarClass("Ford", "Mustang", "Black", "LMN456", minutes_parked=190)
    meter = ParkingMeterClass(minutes_purchased=60)
    officer = PoliceOfficerClass("James Brown", "4321")
    run_and_print(car, meter, officer, "Scenario 3: Car Illegally Parked Past Alotted Time by 130 Minutes")