def Initialise():
    global Jobs, NumberOfJobs
    Jobs = [[-1,-1] for x in range(100)]
    NumberOfJobs = 0

def AddJob(JobNumber, Priority):
    global NumberOfJobs, Jobs
    if NumberOfJobs == 100:
        print("Not added")
    else:
        Jobs[NumberOfJobs] = [JobNumber,Priority]
        print("Added")
        NumberOfJobs += 1

def InsertionSort():
    global Jobs, NumberOfJobs
    for i in range(1, NumberOfJobs):
        Current = Jobs[i] #ARRAY OF INTEGER
        while i > 0 and Jobs[i-1][1] > Current[1]:
            Jobs[i] = Jobs[i-1]
            i -= 1
        Jobs[i] = Current

def PrintArray():
    global Jobs, NumberOfJobs
    for X in range (0, NumberOfJobs) :
        print(str(Jobs[X][0]), " priority " , str(Jobs[X][1]))

Jobs = [] #2D ARRAY OF INTEGER
NumberOfJobs = 0 #INTEGER
Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)
InsertionSort()
PrintArray()