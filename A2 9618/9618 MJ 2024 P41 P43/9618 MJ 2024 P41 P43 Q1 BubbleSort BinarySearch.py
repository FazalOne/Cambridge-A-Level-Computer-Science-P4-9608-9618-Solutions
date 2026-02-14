def Initialise():
    global DataStored, NumberItems
    while NumberItems < 1 or NumberItems > 20:
        NumberItems = int(input("Enter the number of items to be stored (1-20): "))
    DataStored = [int(input("Enter a number: ")) for x in range(NumberItems)]
    
def BubbleSort():
    global DataStored, NumberItems
    length = NumberItems - 1 #INTEGER
    for passes in range(length): #INTEGER
        for compares in range(length - passes): #INTEGER
            if DataStored[compares] > DataStored[compares + 1]:
                temp = DataStored[compares] #INTEGER
                DataStored[compares] = DataStored[compares + 1]
                DataStored[compares + 1] = temp

def BinarySearch(DataToFind):
    global DataStored, NumberItems
    l = 0 #INTEGER
    u = NumberItems - 1 #INTEGER
    while l <= u:
        mid = (l + u) // 2 #INTEGER
        if DataStored[mid] == DataToFind:
            return mid
        if DataStored[mid] < DataToFind:
            l = mid+1
        else:
            u = mid-1
    return -1

DataStored = [] #ARRAY OF INTEGER
NumberItems = 0 #INTEGER
Initialise()
BubbleSort()
print(DataStored)
Search = int(input("Enter a number to find: ")) #INTEGER
if BinarySearch(Search) == -1:
    print("Value not found")
else:
    print("Value found at index ", BinarySearch(Search))