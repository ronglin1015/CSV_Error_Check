import pandas as pd
import os
import datetime as dt
import numpy as np
import csv
import re

# directory
direc = 'G:\Team - Individual Folders\Rong Lin\Python\LIVE'



# list of error strings
strToCheck = ['#VALUE!','N/A','#DIV/0!' ]
# Loop files in the directory and print out files info with error string
for root, dirs, files in os.walk(direc):
    for file in files:
        with open(os.path.join(root, file), "r") as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                for field in row:
                    if field in strToCheck:
                        print(root + file,field)
