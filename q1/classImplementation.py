class FootballPlayer:
    def __init__(self, Name, Age, Club, WagePW):
    self.Name = Name
    self.Age = Age
    self.Club = Club
    self.__WagePW = WagePW

    def DisplayPlayerInfo(self):
        print(f"Name: {self.Name}")
        print(f"Age: {self.Age}")
        print(f"Club: {self.Club}")
        return self.Name, self.Age, self.Club   

     def ShowWages(self):
        wage = len(self.Name) * 1000
        print(f"{self.Name} earns {wage} per week.")
        return wage

    def FollowPlayer(self):
        choose = print(f" Would you like to follow {self.Name}?")
        if choose == True:
            print(f"You are now following {self.Name}")
        elif choose == False:
            print(f"You are not following {self.Name}")
        return choose

FootballPlayer1 = FootballPlayer("Lionel Messi", 36, "Inter Miami")
FootballPlayer2 = FootballPlayer("Cristiano Ronaldo", 38, "Al Nassr")

FootballPlayer1.DisplayPlayerInfo()