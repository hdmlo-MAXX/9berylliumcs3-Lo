class Animal: #Creates the parent class "Animal"
  def __init__(self, name):
    self.name = name

  def make_sound(self): #creates the first attribute
    print(self.name, "makes a sound")

  def eat(self): #creates the second attribute
    print(self.name, "is eating")

class Lion(Animal): #The First Inheriter of the parent function
  def make_sound(self): #overrides the attribute "make_sound"
    print(self.name, "roars loudly!")

  def eat(self): #overrides the attribute "eat"
    print(self.name, "eats Fresh meat")

class Elephant(Animal): #The Second Inheriter of the parent function
  def make_sound(self):
    print(self.name, "trumphets!")

  def eat(self):
    print(self.name, "eats Grass and Fruits.")
    
class Monkey(Animal): #The Third Inheriter of the parent function
  def make_sound(self):
    print(self.name, "chatters!")

  def eat(self):
    print(self.name, "eats Bananas.")

#Initializes the names of the children functions
lion = Lion("Simba") #Simba for the function "Lion(Animal)"
elephant = Elephant("Dumbo") #Dumbo for the function "Elephant(Animal)"
monkey = Monkey("George") #George for the function

lion.make_sound() #prints "Simba roars loudly!"
lion.eat() #prints "Simba  eats fresh meat."
print("-----")
elephant.make_sound() #prints "Dumbo trumphets!"
elephant.eat() #prints "Dumbo eats grass and fruits."
print("-----")
monkey.make_sound() #prints "George chatters!"
monkey.eat() #prints "George eats bananas."
print("-----")
