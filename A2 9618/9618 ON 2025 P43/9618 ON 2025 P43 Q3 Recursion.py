def RecursiveCount(ArrayCopy, NumberElements, DataToFind):
    if len(ArrayCopy) == 0:
        return 0
    if ArrayCopy[0] == DataToFind:
        return 1 + RecursiveCount(ArrayCopy[1:], NumberElements, DataToFind)
    return RecursiveCount(ArrayCopy[1:], NumberElements, DataToFind)

def SplitData(str):
    start = 0 #INTEGER
    SplitArray = [] #ARRAY OF STRING
    for x in range(len(str)):
        if str[x] == ";" :
            SplitArray += [str[start:x]]
            start = x + 1
    if len(SplitArray) < 4:
        print("Sorry, no more lines of code.")
    return SplitArray
    
DataArray = [0,5,1,2,5,9,9,6,5,0] #ARRAY OF INTEGER
print(RecursiveCount(DataArray, 10, 0))
variables = "x=0;y=1;x=x+y;y++;" #STRING
for line in SplitData(variables):
    print(line)