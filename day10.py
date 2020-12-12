import numpy as np
filename = 'day10ex.txt'

with open(filename) as fp:
    content = fp.readlines()
    
for i in range(len(content)):
    content[i] = int(content[i])
    
content.append(max(content)+3)

adapters = np.array(content)
adapters = np.sort(adapters)

differences = []
nearestneighbors = []

for i in range(len(adapters)):
    localneigh = 0
    if i == 0:
        diff = adapters[i]
        if diff > 3:
            print('difference greater than 3 jolts!')
            break
        differences.append(diff)
    else: 
        diff = adapters[i]-adapters[i-1]
        if diff > 3:
            print('difference greater than 3 jolts!')
            break
        differences.append(diff)
        
    if i <= len(adapters)-4:
        localneighs = np.array([adapters[i+1], adapters[i+2], adapters[i+3]])
    
    elif i <= len(adapters)-3:
        localneighs = np.array([adapters[i+1], adapters[i+2]])
    
    elif i <= len(adapters)-2:
        localneighs = np.array([adapters[i+1]])
    print(localneighs)
    numneigh = len(localneighs[localneighs <= adapters[i]+3])
    if numneigh == 3:
        perm = 5
        nearestneighbors.append(perm)
    elif numneigh ==2:
        perm = 2
        nearestneighbors.append(perm)
    else:
        perm = 1
        nearestneighbors.append(perm)
        
    
    
sumt = 0
sumfact = 0
product = 1
for i in range(len(nearestneighbors)):
    if nearestneighbors[i] > 1:
        sumt = sumt+nearestneighbors[i]
        product = product*nearestneighbors[i]
        sumfact = sumfact + np.math.factorial(nearestneighbors[i])
        
            
    
        

numone = differences.count(1)
numtwo = differences.count(2)
numthree = differences.count(3)

print('product of 1s and 3s is: ' + str(numone*numthree))

