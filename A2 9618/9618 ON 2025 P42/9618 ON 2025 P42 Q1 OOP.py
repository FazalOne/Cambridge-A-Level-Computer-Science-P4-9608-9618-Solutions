class Bird:
    def __init__(self, BirdSpecies, BirdDpH):
        self.DistancePerHour = BirdDpH #FLOAT
        self.Species = BirdSpecies #STRING
        self.XPosition = 500.0 #FLOAT
        self.YPosition = 500.0 #FLOAT

    def GetSpecies(self):
        return self.Species
    def GetPosition(self):
        return f"X = {self.XPosition} Y = {self.YPosition}"

    def Move(self, direction, time):
        distance = (self.DistancePerHour / 60) * time #FLOAT
        if direction == "N":
            self.YPosition += distance
        if direction == "S":
            self.YPosition -= distance
        if direction == "E":
            self.XPosition += distance
        if direction == "W":
            self.XPosition -= distance

Bird1 = Bird("Cockatiel",71) #Bird
Bird2 = Bird("Macaw", 56) #Bird

print(Bird1.GetSpecies(), Bird1.GetPosition())
print(Bird2.GetSpecies(), Bird2.GetPosition())
choice = "" #STRING
while choice not in [Bird1.GetSpecies(), Bird2.GetSpecies()]:
    choice = input("Enter your choice of bird: ").title()
for x in [Bird1, Bird2]:
    if choice == x.GetSpecies():
        direction = "" #STRING
        while direction not in ["N","S","E","W"]:
            direction = input("Enter valid direction (N,S,E,W): ").title()
        time = -1 #INTEGER
        while time < 0:
            time = int(input("Enter time traveled: ")) 
        x.Move(direction, time)
        print (f"{x.GetSpecies()} new position is: {x.GetPosition()}")
        break