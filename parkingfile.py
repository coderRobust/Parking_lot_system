import abc
from abc import ABC,abstractmethod 
class Vehicle(ABC):

    def __init__(self, vehicleNo, color, typeOfVehicle):
        self.vehicleNo = vehicleNo
        self.color = color
        self.type = typeOfVehicle
     
    @abstractmethod
    def printInfo(self):
        print('Parked vehicle information is below')
        print(self.vehicleNo)
        print(self.color)
        print(self.type)


class Car(Vehicle):

    def __init__(self, carNo, color, typeOfVehicle):
        super().__init__(carNo, color, typeOfVehicle)

    def printInfo(self):
        super().printInfo()


class Truck(Vehicle):
    def __init__(self, carNo, color, typeOfVehicle):
        super().__init__(carNo, color, typeOfVehicle)

    def printInfo(self):
        super().printInfo()



obj = Car('MP09kl1234', 'Red', 'car')
obj.printInfo()
obj1 = Truck('MP87we123', 'brown', 'Truck')
obj1.printInfo()



