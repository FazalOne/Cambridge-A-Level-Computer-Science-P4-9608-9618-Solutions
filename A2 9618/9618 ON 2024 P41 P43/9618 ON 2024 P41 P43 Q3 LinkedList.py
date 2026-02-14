def InsertData():
    global FirstNode, FirstEmpty, PrevNode
    if FirstEmpty == -1:
        print("The linked list is full")
        return
    for x in range(5):
        if FirstEmpty == -1:
            print("The linked list is full")
            return
        num1 = int(input("Enter a +ve number: ")) #INTEGER
        while num1 < 0:
            num1 = int(input("Enter a +ve number: ")) #INTEGER
        if FirstNode == -1:
            FirstNode = 0
        else:
            LinkedList[PrevNode][1] = FirstEmpty #link prev node to next node
        temp = LinkedList[FirstEmpty][1] #stores next free node
        LinkedList[FirstEmpty][0] = num1 #insert data
        LinkedList[FirstEmpty][1] = -1
        PrevNode = FirstEmpty
        FirstEmpty = temp

def OutputLinkedList():
    currentPointer = FirstNode
    if currentPointer == -1:
        print("Linked list is empty")
    else:
        while currentPointer != -1 and currentPointer != FirstEmpty:
            print("Data {} Pointer {}".format(LinkedList[currentPointer][0], LinkedList[currentPointer][1]))
            currentPointer = LinkedList[currentPointer][1]

def RemoveData(data):
    global FirstNode, FirstEmpty
    if FirstNode == -1:
        print("Sorry, list is empty.")
        return

    Temp = FirstNode
    Temp2 = -1
    while Temp != -1 and LinkedList[Temp][0] != data: # Traverse list for data
        Temp2 = Temp
        Temp = LinkedList[Temp][1]

    if Temp == -1: # If loop finished and Temp is -1, data wasn't found
        print("Data {} does not exist in list".format(data))
        return
    elif Temp == FirstNode:  # Here data is found at head
        FirstNode = LinkedList[Temp][1] # remove at head
    else:
        LinkedList[Temp2][1] = LinkedList[Temp][1] # link prev node to node after Temp

    LinkedList[Temp][0] = -1          
    LinkedList[Temp][1] = FirstEmpty  # Point removed node to current first empty
    FirstEmpty = Temp                 # Make removed node the new FirstEmpty
    print("Data {} found at Index {} and deleted.".format(data, Temp))

FirstEmpty = 0 #INTEGER it is the current free node. headpointer of EmptyList
FirstNode = -1 #INTEGER it is the headpointer of DataList
LinkedList = [[-1,x] for x in range(1,21)] #2D ARRAY OF INTEGER
LinkedList[19] = [-1,-1]

InsertData()
print("Before")
OutputLinkedList()
RemoveData(5)
print("After")
OutputLinkedList()