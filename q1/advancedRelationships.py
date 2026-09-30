class ParentClass:
  def __init__(self, club):
    self.club = club

class ChildClass(ParentClass):
  def __init__(self, club, player):
    super().__init__(club)
    self.player = player

player1 = ChildClass("Ipswich Town", "Enciso")
#Club
print(player1.club)
#Player
print(player1.player)
