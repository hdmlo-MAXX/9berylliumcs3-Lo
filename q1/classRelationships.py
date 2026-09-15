class FootballClub:
    def __init__(self, Name, Stadium, Founded, Fannickname):
        self.Name = Name 
        self.Stadium = Stadium
        self.Founded = Founded
        self.Fannickname = Fannickname

    def ClubInfo(self):
        print(f"Name: {self.Name}")
        print(f"Stadium: {self.Stadium}")
        print(f"Founded: {self.Founded}")
        print(f"Fan Nickname: {self.Fannickname}")
        return self.Name, self.Stadium, self.Founded, self.Fannickname

    def TransferPlayer(self, player):
        print(f"{player.Name} has been transferred to {self.Name}.")
        player.Club = self.Name
        return player.Club

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

FootballClub1 = FootballClub("Inter Miami", "DRV PNK Stadium", 2018, "The Herons")
FootballClub2 = FootballClub("Al Nassr", "Al-Awwal Park", 1955, "Nassrawis")

print("before relationship")
print("Football Player Info:")
FootballPlayer1.DisplayPlayerInfo()
print()
FootballPlayer2.DisplayPlayerInfo()
print()
print("Club Info:")
FootballClub1.ClubInfo()
print()
FootballClub2.ClubInfo()
print()

print("after relationship")
print("Transfers:")
FootballClub.TransferPlayer(FootballClub1, FootballPlayer2)
FootballClub.TransferPlayer(FootballClub2, FootballPlayer1)
print()
print("Football Player Info:")
FootballPlayer1.DisplayPlayerInfo()
print()
FootballPlayer2.DisplayPlayerInfo()
