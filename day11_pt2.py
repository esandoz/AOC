import pandas as pd
import numpy as np

filename = 'day11input.txt'

f = open(filename, "r")
linelength = len(f.readline())-1
f.close()


ff=[1 for i in range(linelength)]
single_data = pd.read_fwf(filename, widths=ff, header=None)

alldata = pd.DataFrame('.', index=np.arange(len(single_data)+2), columns=np.arange(linelength+2))


alldata = alldata.values
olddata = alldata.copy()
numrows = len(single_data)
for i in range(1,len(single_data)+1):
    for j in range(1,linelength+1):
        alldata[i,j] = single_data.iloc[i-1,j-1]

loopcount = 0 

while not np.array_equal(olddata, alldata):
    olddata = alldata.copy()
    for i in range(1,len(single_data)+1):
        for j in range(1,linelength+1):
            testarray = []
            
            rayi =1
            testval = '.'
            while i-rayi >= 1 and testval =='.':
                testval = olddata[i-rayi,j]
                if testval == 'L' or testval == '#':
                    testarray.append(testval)
                    break
                rayi = rayi + 1
                
            rayi =1
            testval = '.'
            while i+rayi <= numrows + 1 and testval =='.':
                testval = olddata[i+rayi,j]
                if testval == 'L' or testval == '#':
                    testarray.append(testval)
                    break
                rayi = rayi + 1
                
            rayj =1
            testval = '.'
            while j-rayj >= 1 and testval =='.':
                testval = olddata[i,j-rayj]
                if testval == 'L' or testval == '#':
                    testarray.append(testval)
                    break
                rayj = rayj + 1
            
            rayj =1
            testval = '.'
            while j+rayj <= linelength+1 and testval =='.':
                testval = olddata[i,j+rayj]
                if testval == 'L' or testval == '#':
                    testarray.append(testval)
                    break
                rayj = rayj + 1
            
            ray =1
            testval = '.'
            while i-ray >=1 and j-ray >=1 and testval == '.':
                testval = olddata[i-ray, j-ray]
                if testval == 'L' or testval == '#':
                    testarray.append(testval)
                    break
                ray = ray + 1
            
            ray =1
            testval = '.'
            while i-ray >=1 and j+ray <= linelength +1 and testval == '.':
                testval = olddata[i-ray, j+ray]
                if testval == 'L' or testval == '#':
                    testarray.append(testval)
                    break
                ray = ray + 1
            
            ray =1
            testval = '.'
            while i+ray <= numrows+1 and j+ray <= linelength +1 and testval == '.':
                testval = olddata[i+ray, j+ray]
                if testval == 'L' or testval == '#':
                    testarray.append(testval)
                    break
                ray = ray + 1
            
            ray =1
            testval = '.'
            while i+ray <= numrows+1 and j-ray >=1 and testval == '.':
                testval = olddata[i+ray, j-ray]
                if testval == 'L' or testval == '#':
                    testarray.append(testval)
                    break
                ray = ray + 1
         
            if alldata[i,j] == 'L' and testarray.count('#') == 0:
                alldata[i,j] = '#'
            elif alldata[i,j] == '#' and testarray.count('#') >= 5:
                alldata[i,j] = 'L'
    loopcount = loopcount + 1
    print('loopcount is ' + str(loopcount))

counter = 0
for i in range(1,len(single_data)+1):
    for j in range(1,linelength+1):
        if alldata[i,j] == '#':
            counter = counter+1

print('the number of occupied seats is: ' + str(counter))

