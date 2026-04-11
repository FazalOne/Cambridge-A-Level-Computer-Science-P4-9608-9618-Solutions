class Record:
    def __init__(self, KeyVal, DataVal):
        self.Key = KeyVal #INTEGER
        self.Data = DataVal #STRING

def InitialiseHashTable():
    global HashTable
    HashTable = [[Record(-1,"") for x in range(10)] for y in range(100)] #2D ARRAY OF Record

def Hash(key):
    return key % 100

def InsertData(NewRecord):
    Value = Hash(NewRecord.Key) #INTEGER
    for x in range(10):
        if HashTable[Value][x].Key == -1:
            HashTable[Value][x] = NewRecord
            break

def ReadData():
    try:
        with open("HashTableData.txt","r") as File:
            for line in File:
                line = line.strip().split(",") #ARRAY OF STRING
                InsertData(Record(int(line[0]), line[1]))
    except FileNotFoundError:
        print("Sorry, file not found.")

def GetRecord(RecordKey):
    Value = Hash(RecordKey) #INTEGER
    for x in range(10):
        if HashTable[Value][x].Key == RecordKey:
            return HashTable[Value][x].Data
    return "Not found"

InitialiseHashTable()
ReadData()
for x in range(5):
    print(GetRecord(int(input("Enter the record key:"))))