import re
import math

filename = 'day12input.txt'

content = []
with open(filename) as fp:
    content = fp.readlines()

instructions = []
for lines in content:
    local = [" ".join(re.split("[^a-zA-Z]", lines)).strip(), int(" ".join(re.split("[^0-9]", lines)).strip())]
    instructions.append(local)

# begin with facing east = 0 degrees, counter clockwise positive
facing = 0
xcoord = 0
ycoord = 0
for i in range(len(instructions)):
    if instructions[i][0] == 'E':
        xcoord = xcoord + instructions[i][1]
    elif instructions[i][0] == 'W':
        xcoord = xcoord - instructions[i][1]
    elif instructions[i][0] == 'N':
        ycoord = ycoord + instructions[i][1]
    elif instructions[i][0] == 'S':
        ycoord = ycoord - instructions[i][1]
    elif instructions[i][0] == 'L':
        facing = facing + instructions[i][1]
    elif instructions[i][0] == 'R':
        facing = facing - instructions[i][1]
    elif instructions[i][0] == 'F':
        xcoord = xcoord + instructions[i][1]*math.cos(facing*math.pi/180)
        ycoord = ycoord + instructions[i][1]*math.sin(facing*math.pi/180)
        

mdistance = round(abs(xcoord) + abs(ycoord)) 
print('Manhattan distance for the boat is: ' + str(int(mdistance)))


xcoord = 0
ycoord = 0
wxcoord = 10
wycoord = 1

#f = open("outputlocations.txt", "w")
#f.close()
#f = open("outputlocations.txt", "a")
for i in range(len(instructions)):
    if instructions[i][0] == 'E':
        wxcoord = wxcoord + instructions[i][1]
    elif instructions[i][0] == 'W':
        wxcoord = wxcoord - instructions[i][1]
    elif instructions[i][0] == 'N':
        wycoord = wycoord + instructions[i][1]
    elif instructions[i][0] == 'S':
        wycoord = wycoord - instructions[i][1]
    elif instructions[i][0] == 'L':
        thet = instructions[i][1]*math.pi/180
        wxcoordold = wxcoord
        wycoordold = wycoord
        wxcoord = round(math.cos(thet)*wxcoordold - math.sin(thet)*wycoordold,0)
        wycoord = round(math.sin(thet)*wxcoordold + math.cos(thet)*wycoordold,0)
    elif instructions[i][0] == 'R':
        thet = -instructions[i][1]*math.pi/180
        wxcoordold = wxcoord
        wycoordold = wycoord
        wxcoord = round(math.cos(thet)*wxcoordold - math.sin(thet)*wycoordold,0)
        wycoord = round(math.sin(thet)*wxcoordold + math.cos(thet)*wycoordold,0)
    elif instructions[i][0] == 'F':
        xcoord = round(xcoord + wxcoord*instructions[i][1],0)
        ycoord = round(ycoord + wycoord*instructions[i][1],0)
#    f.write('xcoord: ' + str(xcoord) + ' ycoord: ' +str(ycoord) +'\n')
#    f.write('wxcoord: ' + str(wxcoord) + ' wycoord: ' +str(wycoord) +'\n\n')
f.close()
mdistance = round(abs(xcoord) + abs(ycoord)) 
print('Manhattan distance for the boat is: ' + str(int(mdistance)))