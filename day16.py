rulesfile = 'day16rules.txt'
neighborsfile = 'day16neighbortickets.txt'
yourticket = 'day16yourticket.txt'

def getrules(rulesfile):
    with open(rulesfile) as fp:
        content = fp.readlines()
    rulelist = []
    for i in range(len(content)):
        linetosplit = content[i].split(': ')
        fieldname = linetosplit[0]
        rangetosplit = linetosplit[1].split(' or ')
        lowerrange = rangetosplit[0].split('-')
        upperrange = rangetosplit[1].split('-')
        lowerset = set(range(int(lowerrange[0]),int(lowerrange[1])+1))
        upperset = set(range(int(upperrange[0]),int(upperrange[1])+1))
        localset = lowerset.union(upperset)
        rulelist.append([fieldname, localset])
        
        if i == 0:
            ruleset = localset
        else:
            ruleset = ruleset.union(localset)
    return ruleset, rulelist


def getneighbors(neighborsfile):
    with open(neighborsfile) as fp:
            content = fp.readlines()
    
    neighborset = []
    neighborlist = []
    for i in range(len(content)):
        linetosplit = [int(x) for x in content[i].split(',')]
        neighborsetlocal = set(linetosplit)
        neighborset.append(neighborsetlocal)
        neighborlist.append(linetosplit)
    
    return neighborset, neighborlist

ruleset, ticketrules = getrules(rulesfile)
neighbors, neighborlist = getneighbors(neighborsfile)


ticketerror = []
goodneighbors = []
for i in range(len(neighbors)):
    localseterror = neighbors[i].difference(ruleset)
    localerror = sum(localseterror)
    ticketerror.append(localerror)
    if len(localseterror) == 0:
        goodneighbors.append(neighborlist[i])

print('the ticket error is: ' + str(sum(ticketerror)))    

def getneighfields(goodneighbors):
    numfields = len(goodneighbors[0])
    fieldlist = []
    for j in range(numfields):
        for i in range(len(goodneighbors)):
            if i == 0:
                fieldset = set([goodneighbors[i][j]])
            else:
                fieldset.add(goodneighbors[i][j])
        fieldlist.append(fieldset)

    return fieldlist

fieldlist = getneighfields(goodneighbors)

fieldvalue = []

for i in range(len(fieldlist)):
    fields = set([])
    for j in range(len(ticketrules)):
        if fieldlist[i].issubset(ticketrules[j][1]):
            fields.add(ticketrules[j][0])
    fieldvalue.append(fields)

isunique = [False for x in fieldvalue]    

while not all(isunique):
    uniquefields = set([])
    for i in range(len(fieldvalue)):
        if len(fieldvalue[i]) == 1:
            uniquefields.update(fieldvalue[i])
            isunique[i] = True
            
    for i in range(len(fieldvalue)):
        if not isunique[i]:
            fieldvalue[i] = fieldvalue[i].difference(uniquefields)

reportvalues = set(['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time'])

def checkticket(yourticket, fieldvalue, reportvalues):
    with open(yourticket) as fp:
        content = fp.readlines()
        linetosplit = [int(x) for x in content[0].split(',')]
        endvalues = []
    fp.close()
    for i in range(len(fieldvalue)):
        if fieldvalue[i].issubset(reportvalues):
            endvalues.append(linetosplit[i])
    
    return endvalues

endvalues = checkticket(yourticket, fieldvalue, reportvalues)
product = 1

for i in range(len(endvalues)):
            product = product*endvalues[i]
print('the sum of the values in my ticket with departures in the field is: ' + str(product))    