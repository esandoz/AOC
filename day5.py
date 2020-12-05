import numpy as np

filename = 'day5input.txt'


def seatfinder(content):
    numhi = 128
    numlow = 0
    for i in range(6):
        if content[i] == 'F':
            numhi = (numhi+numlow)/2
            numlow = numlow
        elif content[i] == 'B':
            numhi = numhi
            numlow = (numhi+numlow)/2
    if content[6] == 'F':
        seatrow = int(numlow)
    elif content[6] == 'B':
        seatrow = int(numhi - 1)
    numhi = 8
    numlow = 0    
    for k in range(7,10):    
        if content[k] == 'L':
            numhi = (numhi+numlow)/2
            numlow = numlow
        elif content[k] == 'R':
            numhi = numhi
            numlow = (numhi+numlow)/2
    if content[9] == 'L':
        seatcol = int(numlow)
    elif content[9] == 'R':
        seatcol = int(numhi - 1)    
    
    seatid = int(seatrow*8 + seatcol) 
    return [seatrow, seatcol, seatid]
        

seatlist = []
with open(filename) as fp:
    for line in fp:
        seatlist.append(seatfinder(line))

seatlist = np.array(seatlist)

print(max(seatlist[:,2]))


seatlist = seatlist[np.argsort(seatlist[:, 2])]

for i in range(1,len(seatlist)):
    if seatlist[i,2]-seatlist[i-1,2] !=1:
        print('missing!')
        print(int((seatlist[i,2]+seatlist[i-1,2])/2))
