import vehicleNew
from vehicleNew import *

class parkingLot(object):

    def __init__(self):

        self.slotId = 0
        self.OccupiedSot = 0
        self.capacity = 0

    def createParkingLot(self, capacity):
        
        self.slots = [-1 for _ in range(capacity)]
        self.capacity = capacity
        return self.capacity

    def getEmptySlot(self):

        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i
        return -1

    def parkVehicle(self, vehicleNo, color, parkstatus, Typeofvehicle = vehicleNew.Car):

        if self.OccupiedSot < self.capacity:

            slotId = self.getEmptySlot()
            if slotId == -1:
                print('No slot avaialable')
                return
            self.slots[slotId] = vehicleNew.Car(vehicleNo,color, parkstatus)
            self.slotId +=1
            self.OccupiedSot +=1
        else:
            return -1

    def leaveVehicle(self, slotId):

        if self.OccupiedSot > 0 and self.slots[slotId - 1] != -1:

            self.slots[slotId - 1] = -1
            self.OccupiedSot -=1
            return True
        return False

    def parkingStatusDisplay(self):
        print('below parking status')
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print('parking lot -> ',self.slots[i].printInfo())
                print('Slot # -', i)
                print('_____________________________\n')
        print('occupied ->',self.OccupiedSot)


def main():

    parkinglot = parkingLot()
    parkinglot.createParkingLot(15)

    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')

    #parkinglot.parkingStatusDisplay()

    parkinglot.leaveVehicle(8)
    parkinglot.leaveVehicle(4)
    parkinglot.leaveVehicle(3)

    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')
    parkinglot.parkVehicle('MP09TD1234', 'RED', 1, 'Car')

    parkinglot.parkVehicle('MP09TD1234', 'white', 1, 'Car')
    parkinglot.parkingStatusDisplay()





if __name__ == '__main__':
	main()










