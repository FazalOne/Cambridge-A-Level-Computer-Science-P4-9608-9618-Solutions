def ReadFile():
    global DataArray
    try:
        with open("IntegerData.txt", 'r') as File:
            for X in range(100):
                DataArray[X] = int(File.readline().strip())
    except FileNotFoundError:
        print("Could not find file")

def FindValues():
    global DataArray
    num = 0 #INTEGER
    while num < 1 or num > 100:
        num = int(input("Enter a number between 1 and 100: "))
    total = 0 #INTEGER
    for x in DataArray:
        if x == num:
            total += 1
    return total

def BubbleSort():
    global DataArray
    N = 100 #INTEGER
    for I in range(N-1):
        for J in range(0, N-I-1):
            if DataArray[J] > DataArray[J+1]:
                DataArray[J], DataArray[J+1] = DataArray[J+1], DataArray[J]
    print(DataArray)

DataArray = [0 for i in range (100)] #ARRAY OF INTEGERS
ReadFile()
print("The number appears ", FindValues(), " times")
BubbleSort()