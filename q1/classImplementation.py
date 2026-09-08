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
        print(f"Wage Per Week: {self.__WagePW}")

    def ShowWages(self):
        return self.__WagePW

ShowWages = FootballPlayer("Jude", 36, "Baby United", 1000000)