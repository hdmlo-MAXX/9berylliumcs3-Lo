# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)

## Existing System Description:
## Inheritance Relationship
Parent: Football Club

Child: Football Player

Explanation: A football player plays for a football club. The information of a football player can be traced back to the football club. 

## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)

## Composition/Aggregation
Relationship: Aggregation/Weak HAS-A relationship

Explanation: A football player can exist without a football club; they are called 'free agents'. 'Free Agents' are player without a club and can be signed by a club without a transfer fee.

## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)

## Python Implementation
[Source Code](advancedRelationships.py)

## Test Run
![Test](images/advancedTestRun.png)

## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
1. Why did you choose your inheritance relationship? Explain why your child class is a type of your
parent class.
2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship
between the two objects.
4. What is the difference between Association from Part III and the advanced relationship you
implemented?
5. How does your design follow the DRY principle?

### Answers:
1. I chose this inheritance relationship because of it's application in the real world. A football player can exist without a club, and a club can exist without a player. The child is a type of parent class because they both contain information from the sport and are similar.
2. Inheritance is like an automatic process in which code is recycled instead of being created. It grabs an already existing code and reuses it for another purpose. The attributes reused are name club.
3. My code is an aggregation relationship because it can exist without the parent function. In the code, the player references the club, but the club can exist independently without the player. Because of this, the lifecycle relationship between the two is independent.
4. The key difference between part III and part IV is the applicated reusing of code. Association determines the relationship between the parent function and child function. Inheritance is the application of the relationship of the functions.
5. The design follows the DRY principle because of the use of inheritance. The design uses delegate attribute assignment in where the 'self.club = club' is delegated to the parent function instead of assigning it again to the child function. because of this, the code is be easily reused and doesn't require duplicate code.
