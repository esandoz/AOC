import pandas as pd
import numpy as np

filename = 'day11input.txt'

f = open(filename, "r")
linelength = len(f.readline())-1
f.close()

ff=[1 for i in range(linelength)]
single_data = pd.read_fwf(filename, widths=ff, header=None)

alldata = pd.DataFrame('.', index=np.arange(len(single_data)+2), columns=np.arange(linelength+2))
olddata = alldata.copy()

for i in range(1,len(single_data)+1):
    for j in range(1,linelength+1):
        alldata.iloc[i,j] = single_data.iloc[i-1,j-1]

loopcount = 0 
while not olddata.equals(alldata):
    olddata = alldata.copy()
    for i in range(1,len(single_data)+1):
    #for i in range(1,2):
        for j in range(1,linelength+1):
            testarray = [olddata.iloc[i-1,j-1], olddata.iloc[i-1,j], olddata.iloc[i-1,j+1], olddata.iloc[i,j-1], olddata.iloc[i,j+1], olddata.iloc[i+1,j-1], olddata.iloc[i+1,j], olddata.iloc[i+1,j+1]]
            if alldata.iloc[i,j] == 'L' and testarray.count('#') == 0:
                alldata.iloc[i,j] = '#'
            elif alldata.iloc[i,j] == '#' and testarray.count('#') >= 4:
                alldata.iloc[i,j] = 'L'
    loopcount = loopcount + 1
    print('loopcount is ' + str(loopcount))

counter = 0
for i in range(1,len(single_data)+1):
    for j in range(1,linelength+1):
        if alldata.iloc[i,j] == '#':
            counter = counter+1

print('the number of occupied seats is: ' + str(counter))

