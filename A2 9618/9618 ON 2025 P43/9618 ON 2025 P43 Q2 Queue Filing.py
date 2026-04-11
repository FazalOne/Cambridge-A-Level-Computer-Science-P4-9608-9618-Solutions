def Enqueue(data):
    global Queue, QueueTail, QueueHead, NumberItems
    if QueueTail == len(Queue) - 1:
        return False
    QueueTail += 1
    if QueueHead == -1:
        QueueHead = QueueTail
    Queue[QueueTail] = data
    NumberItems += 1
    return True

def Dequeue():
    global Queue, QueueHead, QueueTail, NumberItems
    if NumberItems == 0:
        return "False"
    DataToReturn = Queue[QueueHead] #STRING
    QueueHead += 1
    NumberItems -= 1
    return DataToReturn

def ReadData():
    try:
        with open("BinaryData.txt","r") as File:
            for line in File:
                if not Enqueue(line.strip()):
                    print("Sorry, queue is full.")
                    break
    except IOError:
        print("Sorry, there was an issue accessing the file.")

def Compress():
    global NewString #STRING
    counter = 0 #INTEGER
    NewString = "" #STRING
    ReturnValue = Dequeue() #STRING
    while ReturnValue != "False":
        String = ""
        counter = 0 # Reset counter before counting 0s
        while ReturnValue == "0" and ReturnValue != "False":
            counter += 1
            String = "0" + str(counter)
            ReturnValue = Dequeue()
        NewString += String
        String = ""
        counter = 0 # Reset counter before counting 1s
        while ReturnValue == "1" and ReturnValue != "False":
            counter += 1
            String = "1" + str(counter)
            ReturnValue = Dequeue()
        NewString += String
        
def CompressV2():
    global NewString #STRING
    CurrentDigit = Dequeue() #STRING
    NewString = "" #STRING    
    while CurrentDigit != "False":
        StreakCount = 1 #INTEGER
        NextDigit = Dequeue() #STRING
        while NextDigit == CurrentDigit and NextDigit != "False":
            StreakCount += 1 # While next digit matches the current one, we continue counting
            NextDigit = Dequeue() 
        # now streak has ended (either different digit or end of queue)
        RunString = CurrentDigit + str(StreakCount) #STRING
        NewString = NewString + RunString # Create the RLE string
        # now start counting for the next digit
        CurrentDigit = NextDigit

Queue = ["" for x in range(100)] #ARRAY OF STRING
QueueHead = -1 #INTEGER
QueueTail = -1 #INTEGER
NumberItems = 0 #INTEGER
ReadData()
print(Queue)
Compress()
print(NewString)