
class Folder:
    def __init__(self, parent, name, children, size):
        self.parent = parent
        self.name = name
        self.children = children
        self.size = size

def isNumeric(myStr):
    numbers = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
    for char in myStr:
        if char not in numbers:
            return False
    return True


def configureFolderStructure(folder, instructions):
    currentFolder = folder
    for instruction in instructions:
        if len(instruction) == 3: #Change directory
            folderName = instruction[2]
            if  folderName == "..":
                currentFolder = currentFolder.parent
            else:
                currentFolder = currentFolder.children[folderName]

        elif instruction[0] == "dir": #Add folder to folder structure
            newFolder = Folder(currentFolder, instruction[1], {}, 0)
            currentFolder.children[newFolder.name] = newFolder

        elif isNumeric(instruction[0]):
            currentFolder.size += int(instruction[0])


def traverseFolderStructure(currentFolder, folderSizes):
    for folder in currentFolder.children.values():
        currentFolder.size += traverseFolderStructure(folder, folderSizes)
    folderSizes.append(currentFolder.size)
    return currentFolder.size

def getPartOneAns(allFolderSizes):
    sum = 0
    for folderSize in allFolderSizes:
        if folderSize <= 100000:
            sum += folderSize
        else: break
    return sum

def getPartTwoAns(allFolderSizes):
    totalDiskSpace, requiredSpace = 70000000, 30000000
    usedSpace = rootFolder.size
    unusedSpace = totalDiskSpace - usedSpace
    extraSpaceNeeded = requiredSpace - unusedSpace
    for folderSize in allFolderSizes:
        if folderSize >= extraSpaceNeeded:
            return folderSize



with open('/Users/adriancole/Desktop/Advent-Of-Code-2022/day7/input.txt', 'r') as file:
    file_data = file.readlines()
    processed_data = [_.strip() for _ in file_data]

    instructions = [_.split(" ") for _ in processed_data]

    rootFolder = Folder(None, "/", {}, 0)
    configureFolderStructure(rootFolder, instructions[1:])

    allFolderSizes = []
    traverseFolderStructure(rootFolder, allFolderSizes)
    allFolderSizes.sort()

    print(getPartOneAns(allFolderSizes))
    print(getPartTwoAns(allFolderSizes))


