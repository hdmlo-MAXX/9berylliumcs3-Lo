class FootballPlayer:
    def __init__(self, Name, Age, Club, WagePW):
      self.Name = Name
      self.Age = Age
      self.Club = Club
      self.WagePW = WagePW

    def DisplayPlayerInfo(self):
        print(f"Name: {self.Name}")
        print(f"Age: {self.Age}")
        print(f"Club: {self.Club}")
        return self.Name, self.Age, self.Club   

    def ShowWages(self):
        WagePW = len(self.Name) * 1000
        print(f"{self.Name} earns {WagePW} per week.")
        return WagePW

    def FollowPlayer(self):
        choose = input(f"Would you like to follow {self.Name}?: ")
        if choose in ['yes', 'y', 'Yes', 'Y']:
            print(f"You are now following {self.Name}")
            return True
        elif choose in ['no', 'n', 'No', 'N']:
            print(f"You are not following {self.Name}")
            return False
        return choose

FootballPlayer1 = FootballPlayer("Lionel Messi", 36, "Inter Miami", 0)
FootballPlayer2 = FootballPlayer("Cristiano Ronaldo", 38, "Al Nassr", 0)

FootballPlayer1.DisplayPlayerInfo()
FootballPlayer1.ShowWages()
FootballPlayer1.FollowPlayer()

FootballPlayer2.DisplayPlayerInfo()
FootballPlayer2.ShowWages()
FootballPlayer2.FollowPlayer()
