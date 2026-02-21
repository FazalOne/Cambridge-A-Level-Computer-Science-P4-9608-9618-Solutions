class Tree:
    def __init__(self, Name, Growth, Height, Width, Green):
        self.TreeName = Name #STRING
        self.HeightGrowth = int(Growth) #INTEGER
        self.MaxHeight = int(Height) #INTEGER
        self.MaxWidth = int(Width) #INTEGER
        self.Evergreen = Green #STRING
    
    def GetTreeName(self):
        return self.TreeName
    def GetGrowth(self):
        return self.HeightGrowth
    def GetMaxHeight(self):
        return self.MaxHeight
    def GetMaxWidth(self):
        return self.MaxWidth
    def GetEvergreen(self):
        return self.Evergreen
    
def ReadData():
    DataArray = [] #ARRAY OF TREE
    #variant 1
    try:
        with open("Trees.txt", "r") as File:
            DataArray = File.read().split("\n")
        for x in range(9):
            DataArray[x] = DataArray[x].split(",")
            DataArray[x] = Tree(DataArray[x][0], DataArray[x][1], DataArray[x][2], DataArray[x][3], DataArray[x][4])
        return DataArray
    except FileNotFoundError:
        print("Sorry file not found.")
    
    #variant 2
    # DataArray = []
    # try:
    #     with open("Trees.txt") as file:
    #         data = file.readline()
    #         while data != "":
    #             data = data.split(",")
    #             DataArray.append(Tree(data[0],data[1],data[2],data[3],data[4]))
    #             data = file.readline()
    # except FileNotFoundError:
    #     print("Sorry, file not found. Check the filepath.")
    return DataArray
    
def PrintTrees(Tree1):
    out = f"{Tree1.GetTreeName()} has a maximum height {Tree1.GetMaxHeight()}cm, a maximum width {Tree1.GetMaxWidth()}cm, and grows {Tree1.GetGrowth()}cm a year."
    if Tree1.GetEvergreen():
        out += " It does not lose its leaves."
    else:
        out += " It loses its leaves each year."
    print(out)

def ChooseTree(DataArray):
    TreeSearch = [] #ARRAY OF Tree
    height = int(input("Enter the max height of tree: ")) #INTEGER
    width = int(input("Enter the max width of tree: ")) #INTEGER
    evergreen = "" #STRING
    while evergreen not in ["yes","no"]:
        evergreen = input("Do you want an evergreen tree? Yes/No :").lower()

    for TreeObj in DataArray:
        if TreeObj.GetMaxHeight() <= height and TreeObj.GetMaxWidth() <= width and TreeObj.GetEvergreen().lower() == evergreen:
            TreeSearch.append(TreeObj)
            PrintTrees(TreeObj)
    if len(TreeSearch) == 0:
        print("Sorry, no trees meet your requirements.")
    else:
        found = False
        while not found:
            chosentree = input("Enter the name of the tree you have chosen: ") #STRING
            for TreeObj in TreeSearch:
                if TreeObj.GetTreeName().title() ==  chosentree.title():
                    found = True
                    chosentree = TreeObj
                    break
            if not found:
                print("Sorry, your chosen tree does not exist. Input the correct name. ")
        buyheight = int(input("Enter the height of the tree at purchase: ")) #INTEGER
        while buyheight > chosentree.GetMaxHeight():
            buyheight = int(input("Sorry, the height is greater than the tree's max height. Please enter a valid height: ")) #INTEGER
        time = (chosentree.GetMaxHeight() - buyheight) / chosentree.GetGrowth() #REAL
        print(f"{chosentree.GetTreeName()} will take {time} years to reach its maximum height of {chosentree.GetMaxHeight()}cm. ")

Trees = ReadData() #ARRAY OF Tree
PrintTrees(Trees[0])
ChooseTree(Trees)