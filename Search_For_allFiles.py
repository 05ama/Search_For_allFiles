from os import listdir
from os.path import isfile, join

import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("Please input your searching directory: ")
    source_dir = input()
    print("Please input your searching tag: ")
    tag = input()
    onlyfiles =[]
    path_to_search = [source_dir]

    def search_folders(directory,path):
        for object in listdir(directory) :
            if isfile(join(directory, object)):
                if tag in object:
                    onlyfiles.append(join(directory, object))
            else:
                path.append(join(directory, object))

    for directory in path_to_search:
        search_folders(directory,path_to_search)

    print(onlyfiles)
    input()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


