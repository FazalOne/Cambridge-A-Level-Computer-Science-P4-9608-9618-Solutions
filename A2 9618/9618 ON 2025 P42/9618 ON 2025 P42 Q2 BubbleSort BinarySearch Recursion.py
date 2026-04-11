import random
def PrintArray(data):
    for x in data:
        print(x, end = " ")
    print()

def BubbleSort(data):
    for passes in range(len(data) - 1):
        for compares in range(len(data) - passes - 1):
            if data[compares] > data[compares + 1]:
                temp = data[compares] #INTEGER
                data[compares] = data[compares + 1]
                data[compares + 1] = temp
    return data

def RecursiveBinarySearch(DataArray, Lower, Upper, Search):
    if Lower > Upper:
        return -1
    Mid = (Lower + Upper) // 2 #INTEGER
    if DataArray[Mid] == Search:
        return Mid
    if DataArray[Mid] < Search:
        return RecursiveBinarySearch(DataArray, Lower + 1, Upper, Search)
    if DataArray[Mid] > Search:
        return RecursiveBinarySearch(DataArray, Lower, Upper - 1, Search)

DataArray = [-1 for x in range(20)] #ARRAY OF INTEGER
for x in range(20):
    y = -1 #INTEGER
    while y in DataArray:
        y = random.randint(0,100)
    DataArray[x] = y
print("Unsorted")
PrintArray(DataArray)
DataArray = BubbleSort(DataArray)
print("Sorted")
PrintArray(DataArray)
Search = int(input("Enter number to search: ")) #INTEGER
ReturnVal = RecursiveBinarySearch(DataArray, 0, len(DataArray)-1, Search) #INTEGER
if ReturnVal != -1:
    print("Found at position", ReturnVal)
else:
    print("Not Found")