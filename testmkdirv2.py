# this program asks which type of files you will be moving #
# it then checks if a directory with that respective name exists #
# if directory does not exist, it then creates said directory #
# and moves all files of that type to that directory #

import os
from os import listdir
from os.path import isfile, join
import shutil

mypath = os.path.join(os.path.expanduser('~'), 'Desktop') # you can substitute 'Desktop' with whatever folder files are in after user folder
new_path = input('Hello, please choose extension type to \nmove   (py, exe, jpg, png, zip, etc.):')

# check for file path
if os.path.exists(new_path):
    # creates variable from all files from path's directory
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))] 
    for files in onlyfiles:
        if files.endswith(new_path):
            print('These files were moved: ', files)
            shutil.move(files, new_path)
# creates directory and moves files
else:
    os.mkdir(mypath + '\\' + new_path)
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for files in onlyfiles:
        if files.endswith(new_path):        
            print('These files were moved: ', files)
            shutil.move(files, new_path) 
    

