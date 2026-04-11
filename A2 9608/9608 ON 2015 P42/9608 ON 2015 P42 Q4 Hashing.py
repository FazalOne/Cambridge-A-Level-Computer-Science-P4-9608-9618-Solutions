def CreateDictionary():
    Dictionary = [["" for _ in range(2)] for _ in range(2000)] #2D ARRAY OF STRINGS
    return Dictionary

def Hash(key):
    number = ord(key[0]) - 64 #INTEGER
    return number

def Add(newkey, newvalue):
    index = Hash(newkey) #INTEGER
    while dictionary[index][0] > "":
        index += 1
        if index >= 2000:
            index = 0 
    dictionary[index] = [newkey,newvalue]

def Delete(deletekey):
    index = Hash(deletekey) #INTEGER
    while dictionary[index][0] != deletekey:
        index += 1
        if index >= 2000:
            index = 0
    dictionary[index] = ["",""]

dictionary = CreateDictionary() #2D ARRAY OF STRINGS
Add("File", "Datei")
Add("Disk", "Platte")
Add("Error", "Fehler")
Add("Computer", "Rechner")
Delete("Disk")
for entry in dictionary:
    if entry[0] != "":
        print(f"Key: {entry[0]}, Value: {entry[1]}")