class Club:
  def __init__(self, name):
    self.name = name

class Player:
  def __init__(self, name, club):
    self.name = name
    self.club = club
    
ipswich = Club("Ipswich Town")
player1 = Player("Enciso", ipswich)

print(player1.club.name)
print(player1.name)       
