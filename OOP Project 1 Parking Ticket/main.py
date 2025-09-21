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
