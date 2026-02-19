def IterativeVowels(Value):
    Total = 0 #INTEGER
    for x in range(0, len(Value)):
        if Value[x] in ['a','e','i','o','u']:
            Total += 1
    return Total

def RecursiveVowels(Value):         #method 1 using slicing
    if len(Value) == 0:
        return 0
    if Value[0] in ['a','e','i','o','u']:
        return 1 + RecursiveVowels(Value[1:])
    return 0 + RecursiveVowels(Value[1:])

def newRecursiveVowels(Value, x):   #method 2 using index
    if x == len(Value):
        return 0
    if Value[x] in ['a','e','i','o','u']:
        return 1 + newRecursiveVowels(Value, x + 1)
    return 0 + newRecursiveVowels(Value, x + 1)

print(IterativeVowels("house"))
print(RecursiveVowels("imagine"))
print(newRecursiveVowels("imagine", 0))