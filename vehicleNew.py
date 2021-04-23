import abc
from abc import ABC, abstractmethod
import enum


class ParkingStatus(enum.Enum):
    PARKED, RELEASED = 1, 0

class Vehicle(ABC):

    def __init__(self, vehicleNo, color, parkstatus, vehicleType):

        self.vehicleNo = vehicleNo
        self.color = color
        self.parkstatus = parkstatus
        self.vehicleType = vehicleType

    @abstractmethod
    def printInfo(self):
        print('your parked vehicle information')
        print('vehicle # - >', self.vehicleNo)
        print('color ->', self.color)
        print('park status ->', self.parkstatus)
        print('vehicle type ->', self.vehicleType)

class Car(Vehicle):

    def __init__(self, vehicleNo, color, ParkingStatus = ParkingStatus.PARKED, vehicleType = 'CAR'):
        super().__init__(vehicleNo, color, ParkingStatus, vehicleType)

    def printInfo(self):
        super().printInfo()

class Truck(Vehicle):

    def __init__(self, vehicleNo, color, ParkingStatus = ParkingStatus.PARKED, vehicleType = 'TRUCK' ):
        super().__init__(vehicleNo, color, ParkingStatus, vehicleType)

    def printInfo(self):
        super().printInfo()


# car1 = Car('MP0921321', 'RED', 0 )
# truck1 = Truck('MP443221', 'Brown', 1)

# car1.printInfo()
# truck1.printInfo()







