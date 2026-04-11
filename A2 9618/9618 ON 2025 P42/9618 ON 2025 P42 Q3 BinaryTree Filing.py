def AddNode(data):
    global TreeArray, RootPointer, FreeNode
    if FreeNode <= 49:
        TreeArray[FreeNode] = [-1,data,-1]
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False #BOOLEAN
            CurrentNode = RootPointer #INTEGER
            while not Placed:
                if data < TreeArray[CurrentNode][1]:
                    if TreeArray[CurrentNode][0] == -1:
                        TreeArray[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = TreeArray[CurrentNode][0]
                else:
                    if TreeArray[CurrentNode][2] == -1:
                        TreeArray[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = TreeArray[CurrentNode][2]
        FreeNode += 1
    else:
        print("The tree is full")

def WriteAllToFile():
    global TreeArray
    try:
        with open("Tree.txt","w") as File:
            for Line in TreeArray:
                File.write(f"{Line[0]},{Line[1]},{Line[2]}\n")
    except IOError:
        print("Sorry, there was an issue while writing to the file.")

TreeArray = [[-1,-1,-1] for y in range(50)] #2D ARRAY OF INTEGER
RootPointer = -1 #INTEGER
FreeNode = 0 #INTEGER
try:
    with open("TreeData.txt","r") as File:
        for Line in File:
            AddNode(int(Line.strip()))
except IOError:
    print("Sorry, there was an issue while opening the file.")
WriteAllToFile()