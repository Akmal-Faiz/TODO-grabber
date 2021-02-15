import glob
import os

# list all files in this and all children directories
def listFiles(path='./'):
    res = []
    
    # if current path is a file, return it
    if os.path.isfile(path):
        return [path]

    # skip this file
    if 'todoGrabber' in path:
        return res

    children = (glob.glob(path+'/*'))
    
    for child in children:
        if 'todoGrabber.py' in child:
            continue # ignore this file
        res += listFiles(child)
    return res
    
# check if a file contains the string "TODO"
def checkTODO(filePath):
    try:
        s = open(filePath).read()
    except UnicodeDecodeError: 
        return False #skip non-text files
    if 'TODO' in s:
        return True
    return False

def grabTODOs(path = os.getcwd()):
    res = []
    files = listFiles(path)
    
    for f in files:
        if checkTODO(f):
            print(f)
            res.append(f)
    return res

if __name__ == '__main__':
    curr_dir = os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1])
    grabTODOs(path=curr_dir)