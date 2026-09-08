**# SG4 - Understanding Classes and Objects**

## Class Name : FootballPlayer

## Class Description :The basic information about a Football Player

 Properties --
| Property | Data Type | Description |
|---| ---|---|
| +Name     | String    | The name of the Football Player |
| +Age      | Integer   | The number of years the Player has lived |
| +Club     | String    | The current club the Player is playing for |
| -WagePW   | Integer   | The Amount of money the player earns per week at the club |

Methods --
| Name | Description |
|---|---|
| +DisplayPlayerInfo() | Displays the Player and his Information |
| +ShowWages() | Shows the wage per week of a person that's hidden in the public player information |
| +FollowPlayer(Yes or No: Boolean) | Allows you to become a fan of the player and support him in his future matches |

## Class Diagram --
![Class Diagram](<Screenshot 2026-09-01 130755.png>)

## Design Explanation
### Why did you choose this class?
#### I chose this class I love the sport of Football(Soccer). Every country has their own professional Football league and the most popular sport in the world. There are a lot of players around the world who each play for their own club. Their performances on the pitch decide their future, social popularity, and statistics that affect their portfolio when planning to leave or transfers to another club. The properties and methods all give the basic information of the player as well as the ability to follow and the support the player if needed.

### Which property is the most important? Why?
#### The most important property would be the Club. As there are many footballers around the globe, there are going to be a lot of name-a-likes that play for different clubs. By finding the club that the player plays for, identifying the footballer your looking for is going to be easier.

### Which method is the most useful? Why?
#### The most useful method would be the FollowPlayer method. After looking at everything the football player has to offer, the user can decide whether to follow the player or not. The FollowPlayer method will allow the ability to follow future matches of the player without the need to find another external site that also does the same, which can be time consuming.

# Part 2
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Name | string | + | People must know the player's name in order to identify and know more about the player |
| Age | integer | + | So people know how old the player is and base their criticism on the player's performance at that age |
| Club | string | + | People must know the player's club in order to identify the club the player plays for and reduce confusion with a player of the same name as another player |
| WagePW | integer | - | Because wage is not a necessary public information to know about a player  |

## Design Revision
Changes from my previous design:
YearJoined to WagePW
DisplayG/A() to ShowWages()
DisplayAppearances() to DisplayPlayerInfo()
