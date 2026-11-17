#Answers to the questions:
#1. Duck typing is another way to achieve Polymorphism without using inheritance. The object must have the minimum neccessary attributes/methods.
#2. The function of the car was renamed from "horn" to "speak". This is because of the analogy, "If it looks like a duck, and quacks like a duck, then it is a duck." PYthon thinks that since the function was now named "speak", then the car must also speak like the other classes.

class Car: #Creates the class "Car"
  def move(self):
    print("The car drives on the road.")

class Boat: #Creates the class "Boat"
  def move(self):
    print("The boat sails on water.")

class Drone: #Creates the class "Drone"
  def move(self):
    print("The drone flies in the sky.")

def start_trip(vehicle): #Creates a function that calls for the method "move"
    vehicle.move()

car = Car() #Creates the objects
boat = Boat()
drone = Drone()

start_trip(car) #The function calls for the method "move" inside of the object containing the class
start_trip(boat)
start_trip(drone)

#3. The code demonstrates Polymorphism through the function "move". Even though each class has its own distinct name, the function is what connects all three of them into a similar category Python recognizes. Thus demonstrating Polymorphism.
