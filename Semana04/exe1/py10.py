import os
from datetime import datetime

os.chdir('/Users/wander/Desktop')

for dirpath, dirnames, filenames in os.walk('/Users/wander/Desktop'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
