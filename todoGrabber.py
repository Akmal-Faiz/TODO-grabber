import glob

# list all files in this and all children directories
def listFiles(path):
    return []

# check if a file contains the string "TODO"
def checkTODO(filePath):
    pass

def grabTODOs(path = './'):
    res = []
    files = listFiles(path)
    for f in files:
        if checkTODO(f):
            print(f)
    return res

if __name__ == '__main__':
    grabTODOs()