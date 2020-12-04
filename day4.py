import pandas as pd

filename = 'day4input.txt'

certlist=[]
lineold = ''
with open(filename) as fp:
    content = fp.readlines()

# this combines multiple lines for passports into a single line with the blank line '\n' as the delimiter
for i in range(len(content)):
    if content[i] == '\n':
        certlist.append(lineold)
        lineold = ''
    else: 
        lineold = lineold + content[i]
#certlist.append(lineold)

def testfield(document):
    if 'byr' in document and 'iyr' in document and 'eyr' in document and 'hgt' in document and 'hcl' in document and 'ecl' in document and 'pid' in document:
        return True

def testbyr(document):
    if len(document.split(sep='byr:')[1].split(sep='\n')[0]) < len(document.split(sep='byr:')[1].split(sep=' ')[0]):
        byr = document.split(sep='byr:')[1].split(sep='\n')[0]
    else: 
        byr = document.split(sep='byr:')[1].split(sep=' ')[0] 
    if len(byr) == 4 and int(byr) <= 2020 and int(byr) >=1920:
        return True
    else:
        return False

def testiyr(document):
    if len(document.split(sep='iyr:')[1].split(sep='\n')[0]) < len(document.split(sep='iyr:')[1].split(sep=' ')[0]):
        iyr = document.split(sep='iyr:')[1].split(sep='\n')[0]
    else: 
        iyr = document.split(sep='iyr:')[1].split(sep=' ')[0]
    
    if len(iyr) == 4 and int(iyr) <= 2020 and int(iyr) >=2010:
        return True
    else:
        return False
    
def testeyr(document):
    if len(document.split(sep='eyr:')[1].split(sep='\n')[0]) < len(document.split(sep='eyr:')[1].split(sep=' ')[0]):
        eyr = document.split(sep='eyr:')[1].split(sep='\n')[0]
    else: 
        eyr = document.split(sep='eyr:')[1].split(sep=' ')[0]        
    if len(eyr) == 4 and int(eyr) <= 2030 and int(eyr) >=2020:
        return True
    else:
        return False
    
def testhgt(document):
    if len(document.split(sep='hgt:')[1].split(sep='\n')[0]) < len(document.split(sep='hgt:')[1].split(sep=' ')[0]):
        hgt = document.split(sep='hgt:')[1].split(sep='\n')[0]
    else: 
        hgt = document.split(sep='hgt:')[1].split(sep=' ')[0] 
    if 'cm' in hgt:
        if int(hgt.replace('cm','')) <= 193 and int(hgt.replace('cm','')) >= 150:
            return True
    elif 'in' in hgt:
        if int(hgt.replace('in','')) <= 76 and int(hgt.replace('in','')) >=59:
            return True
    else: 
        return False

def testhcl(document):
    if len(document.split(sep='hcl:')[1].split(sep='\n')[0]) < len(document.split(sep='hcl:')[1].split(sep=' ')[0]):
        hcl = document.split(sep='hcl:')[1].split(sep='\n')[0]
    else: 
        hcl = document.split(sep='hcl:')[1].split(sep=' ')[0]
    listhcl = []
    acceptlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for n in range(1,len(hcl)):
        listhcl.append(hcl[n])
    if hcl[0] == '#' and len(hcl) == 7 and set(listhcl).issubset(set(acceptlist)):
        return True
    else:
        return False

def testecl(document):
    if len(document.split(sep='ecl:')[1].split(sep='\n')[0]) < len(document.split(sep='ecl:')[1].split(sep=' ')[0]):
        ecl = document.split(sep='ecl:')[1].split(sep='\n')[0]
    else: 
        ecl = document.split(sep='ecl:')[1].split(sep=' ')[0]
    acceptlist = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if len(ecl) == 3 and ecl in acceptlist:
        return True
    else:
        return False

def testpid(document):
    if len(document.split(sep='pid:')[1].split(sep='\n')[0]) < len(document.split(sep='pid:')[1].split(sep=' ')[0]):
        pid = document.split(sep='pid:')[1].split(sep='\n')[0]
    else: 
        pid = document.split(sep='pid:')[1].split(sep=' ')[0]
    if pid.isnumeric() and len(pid)==9:
        return True
    else: 
        return False

    
countcert = [0 for n in range(len(certlist))]
for i in range(len(certlist)):
    document = certlist[i]
    if testfield(document):
        if all([testbyr(document), testiyr(document), testeyr(document), testhgt(document), testhcl(document), testecl(document), testpid(document)]): 
            countcert[i]=1       

        
print(sum(countcert))

