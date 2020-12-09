import copy
filename = 'day8input.txt'

with open(filename) as fp:
    content = fp.readlines()

codelinesplit = []
for i in range(len(content)):
    codeline = content[i].split(' ')
    codeline[1] = int(codeline[1].replace('\n',''))
    codelinesplit.append(codeline)

nobreaker = False

def loopcounter(codelinesplit, nobreaker):
    j=0
    pastj = []
    accumulator = 0
    while j < len(codelinesplit):
        pastj.append(j)
        if codelinesplit[j][0] == 'acc':
            accumulator = accumulator + codelinesplit[j][1]
            j = j + 1
            if j in pastj:
                break
            if j >= len(codelinesplit):
                nobreaker = True
                break
        elif codelinesplit[j][0] == 'jmp':
            j = j + codelinesplit[j][1]
            if j in pastj:
                break
            if j >= len(codelinesplit):
                nobreaker = True
                break
        elif codelinesplit[j][0] == 'nop':
            j = j + 1
            if j in pastj:
                break
            if j >= len(codelinesplit):
                nobreaker = True
                break
    return ([accumulator, nobreaker])


print('the accumulator value before the infinite loop begins is: ' + str(loopcounter(codelinesplit, nobreaker)[0]))


for i in range(len(codelinesplit)):
    newcodelinesplit = copy.deepcopy(codelinesplit) #this is really stupid but a list of lists cannot be copied to another list without the two lists being linked (modifications to list b will modify list a if b = a)
    if newcodelinesplit[i][0] == 'nop':
        if newcodelinesplit[i][1] != 0:
            newcodelinesplit[i][0] = 'jmp'
    elif newcodelinesplit[i][0] == 'jmp':
        newcodelinesplit[i][0] = 'nop'
    testloop = loopcounter(newcodelinesplit, nobreaker)
    nobreaker = testloop[1]
    if nobreaker:
        print('the accumulator value after successful repair is: ' + str(testloop[0]))
        break
   