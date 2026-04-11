def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    RecursiveInsertion(IntegerArray, NumberElements - 1)
    LastItem = IntegerArray[NumberElements - 1] #INTEGER
    CheckItem = NumberElements - 2 #INTEGER
    while CheckItem >= 0 and IntegerArray[CheckItem] >= LastItem:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem -= 1
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

def IterativeInsertion(IntegerArray, NumberElements):
    for i in range(1, NumberElements):
        LastItem = IntegerArray[i] #INTEGER
        CheckItem = i - 1 #INTEGER
        while CheckItem >= 0 and IntegerArray[CheckItem] >= LastItem:
            IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
            CheckItem -= 1
        IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

def BinarySearchRecursive(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    Middle = (Last + First) // 2 #INTEGER
    if IntegerArray[Middle] == ToFind:
        return Middle
    elif IntegerArray[Middle] > ToFind:
        return BinarySearchRecursive(IntegerArray, First, Middle - 1, ToFind)
    else:
        return BinarySearchRecursive(IntegerArray, Middle + 1, Last, ToFind)

NumberArray1 = [100, 85, 644, 22, 15, 8, 1] #ARRAY OF INTEGER
NumberArray2 = [100, 85, 644, 22, 15, 8, 1] #ARRAY OF INTEGER 
SortedArray = RecursiveInsertion(NumberArray1, len(NumberArray1))
print("Recursive", SortedArray)
SortedArray = IterativeInsertion(NumberArray2, len(NumberArray2))
print("Iterative", SortedArray)
Position = BinarySearchRecursive(NumberArray1, 0, len(NumberArray1)-1, 644)
if Position == -1:
    print("Not found")
else:
    print(Position)

# lists are passed by reference and modified in place in Python 
# As code reaches line38 IterativeInsertion(NumberArray)), it passes already sorted list..
# So we create an array copy NumberArray2, to show that IterativeInsertion correctly sorts an unsorted list