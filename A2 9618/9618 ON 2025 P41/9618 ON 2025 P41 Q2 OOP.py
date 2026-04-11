class Train:
    def __init__ (self, TrainID, RouteNum):
        self.TrainIDNumber = TrainID #STRING
        self.Route = RouteNum #INTEGER
    def GetTrainIDNumber(self):
        return self.TrainIDNumber
    def GetRoute(self):
        return self.Route
    
class Station:
    def __init__(self, StatID, NoPlatform):
        self.StationID = StatID #STRING
        self.NumberPlatforms = NoPlatform #INTEGER
        self.Trains = [] #ARRAY OF Train
        self.NumberTrains = 0 #INTEGER

    def AddTrain(self, NewTrain):
        if self.NumberPlatforms > self.NumberTrains and len(self.Trains) < 10:
            self.Trains.append(NewTrain)
            self.NumberTrains += 1
            return True
        return False
    def GetTrains(self):
        if self.NumberTrains == 0:
            return "There are no trains"
        out = f"The trains at station {self.StationID} are:"
        for train in self.Trains:
            out += f"\n{train.TrainIDNumber} on route number {train.Route}"
        return out

Train1 = Train("12ADV",134) #Train
Train2 = Train("33ART",20) #Train
Train3 = Train("9FKF",3) #Train
Train4 = Train("21VBC",24) #Train
Station1 = Station("STH",2) #Station
Station2 = Station("NTH",1) #Station

STHTrains = [Train1, Train2, Train3] #ARRAY OF Train
NTHTrains = [Train4] #ARRAY OF Train
for train in STHTrains:
    if not Station1.AddTrain(train):
        print("Sorry, station is full")
for train in NTHTrains:
    if not Station2.AddTrain(train):
        print("Sorry, station is full")

print(Station1.GetTrains())
print(Station2.GetTrains())