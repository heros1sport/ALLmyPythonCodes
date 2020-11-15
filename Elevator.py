import winsound
import time
class Elevator:
    floor = 1
    wantedFloor = 3
    floors = list(range(1,6))
    floorNames = ["Clinic","Saloon","Mall","Cinema","Hotel Rooms"]
    def greetings():
        print("""


                    Greetings passenger, what floor would you like to go to?


              """)
    def getInputFloor():
        Elevator.wantedFloor = input("Type floor no.")
    def getFloorNames():
        i = 0
        while i != int(Elevator.floors[-1]):
            print(str(Elevator.floors[i]) + "." + Elevator.floorNames[i] + "\n")
            i += 1
        del i
    def ElevatorActionUp():
        print("Ding!")
        winsound.PlaySound("C:/Users/Guest/Desktop/python projects and pygame games/shift.wav",winsound.SND_ASYNC)
        time.sleep(2)
        while Elevator.floor != int(Elevator.wantedFloor):
            print("Floor " + str(Elevator.floor) + " passes")
            Elevator.floor += 1
            time.sleep(2)
        time.sleep(2)
        print("Ding!")
        winsound.PlaySound("C:/Users/Guest/Desktop/python projects and pygame games/shift.wav",winsound.SND_ASYNC)
        time.sleep(1)
        print("You have reached your destination")
        time.sleep(2)
        print("This is floor " + str(Elevator.floor) + ", And the floor name is " + Elevator.floorNames[Elevator.floor-1])
    def ElevatorActionDown():
        print("Ding!")
        winsound.PlaySound("C:/Users/Guest/Desktop/python projects and pygame games/shift.wav",winsound.SND_ASYNC)
        time.sleep(2)
        while Elevator.floor != int(Elevator.wantedFloor):
            print("Floor " + str(Elevator.floor) + " passes")
            Elevator.floor -= 1
            time.sleep(2)
        time.sleep(2)
        print("Ding!")
        winsound.PlaySound("C:/Users/Guest/Desktop/python projects and pygame games/shift.wav",winsound.SND_ASYNC)
        time.sleep(1)
        print("You have reached your destination")
        time.sleep(2)
        print("This is floor " + str(Elevator.floor) + ", And the floor name is " + Elevator.floorNames[Elevator.floor-1]) 
switch = 0
while switch != 1:
    Elevator.greetings()
    time.sleep(2)
    Elevator.getFloorNames()
    time.sleep(2)
    Elevator.getInputFloor()
    if Elevator.wantedFloor == 'exit':
        switch = 1
    if int(Elevator.wantedFloor) > 5:
        print("Floor should not be more than 5")
    elif int(Elevator.wantedFloor) < 0:
        print("Floor should not be less than 1")
    elif Elevator.floor < int(Elevator.wantedFloor):
        Elevator.ElevatorActionUp()
    elif Elevator.floor > int(Elevator.wantedFloor):
        Elevator.ElevatorActionDown()
    
    time.sleep(2)
quit()
