import random
def Push(data):
    global TopOfStack
    if TopOfStack == 29:
        return False
    TopOfStack += 1
    Stack[TopOfStack] = data
    return True

def Pop():
    global TopOfStack
    if TopOfStack == -1:
        return -999
    data = Stack[TopOfStack] #INTEGER
    TopOfStack -= 1
    return data

def FindValues():
    largest = 0 #INTEGER
    smallest = 1000 #INTEGER
    data = Pop() #INTEGER
    if data == -999:
        print("Stack is empty")
    else:
        while data != -999:
            if data > largest:
                largest = data
            if data < smallest:
                smallest = data
            data = Pop()
        print("The largest value is:", largest)
        print("The smallest value is:", smallest)

Stack = [-1 for x in range(30)] #ARRAY OF INTEGER
TopOfStack = -1 #INTEGER
for x in range(40):
    if not Push(random.randint(0,1000)):
        print("Stack full")
        break
FindValues()