# Class Attributes and Methods

## Previous Design

Link to my previous activity:
[classobjectUML.md](classobjectUML.md)

## Design Revision
Describe any changes made to your original class.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Name | string | + | People must know the player's name in order to identify and know more about the player |
| Age | integer | + | So people know how old the player is and base their criticism on the player's performance at that age |
| Club | string | + | People must know the player's club in order to identify the club the player plays for and reduce confusion with a player of the same name as another player |
| WagePW | integer | - | Because wage is not a necessary public information to know about a player  |

## Updated UML Class Diagram
![Class Diagram](q1/image.png)

## Python Implementation
[View Python Source](classImplementation.py)

## Test Run
![Test Run](q1/classTestRun.png)

## Object Diagram
![Object Diagram](q1/objectDiagram.png)

## Analysis
### Why did you make your chosen attribute private?
### Which method changes the state of your object?
### How did your two objects demonstrate that instances are independent?
### What is the difference between your class diagram and your object diagram?
