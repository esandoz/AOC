filename = 'day9input.txt'

with open(filename) as fp:
    content = []
    for line in fp:
        content.append(int(line))
        

preamble = 25

def numchecker(numarray, arrayindex, preamble):
    testvalue = numarray[arrayindex]
    testarray = []
    for j in range(arrayindex-1, arrayindex-preamble-1, -1):
        for k in range(j-1, arrayindex-preamble-1, -1):
            testarray.append(numarray[k] + numarray[j])
    if testvalue not in testarray:
        print('the number that does not meet the cypher requirements is: ' + str(testvalue))
        return testvalue

for i in range(preamble, len(content)):
    testnumber = numchecker(content, i, preamble)
    if testnumber != None:
        invalidnumber = testnumber
        


for i in range(len(content)):
    if content[i] == invalidnumber:
        continue
    
    sumtest = 0
    counter = 0
    sumarray = []
    while sumtest < invalidnumber:
        sumarray.append(content[i+counter])
        sumtest = sum(sumarray)
        counter = counter + 1
    if sumtest == invalidnumber:
        print('the sum of the max and min values in the continuous set that add up to the invalid number is: ' + str(max(sumarray)+min(sumarray)))
    