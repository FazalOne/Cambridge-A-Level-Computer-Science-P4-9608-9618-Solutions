class BoardObject:
    def __init__(self, ObjCode, ObjValue):
        self.Code = ObjCode #STRING
        self.Value = ObjValue #INTEGER
    def GetCode(self):
        return self.Code
    def GetValue(self):
        return self.Value
    
class Board:
    def __init__(self):
        self.TheBoard = [[BoardObject("-",0) for x in range(10)] for y in range(10)] #2D ARRAY OF BoardObject
    def GetObject(self, row, col):
        return self.TheBoard[row][col]
    def SetObject(self, ObjNew, row, col):
        self.TheBoard[row][col] = ObjNew

    def DisplayBoard(self):
        for row in self.TheBoard:
           for col in row:
               print(col.GetCode(), end = " ")
           print()

Object1 = BoardObject("A",2) #BoardObject
Object2 = BoardObject("B",3) #BoardObject
Object3 = BoardObject("C",5) #BoardObject
Object4 = BoardObject("D",2) #BoardObject
Object5 = BoardObject("E",7) #BoardObject
GameBoard = Board() #Board
GameBoard.SetObject(Object1, 0, 0)
GameBoard.SetObject(Object2, 9, 9)
GameBoard.SetObject(Object3, 4, 5)
GameBoard.SetObject(Object4, 2, 2)
GameBoard.SetObject(Object5, 8, 7)
GameBoard.DisplayBoard()
rowInput = -1 #INTEGER
colInput = -1 #INTEGER
while not (0 <= rowInput <= 9 and 0 <= colInput <= 9):
    rowInput = int(input("Enter valid row (0-9): "))
    colInput = int(input("Enter valid column (0-9): "))
if GameBoard.GetObject(rowInput, colInput).GetCode() != "-":
    print(GameBoard.GetObject(rowInput, colInput).GetCode(), GameBoard.GetObject(rowInput, colInput).GetValue())
else:
    print("Miss")