import re 
filename = 'day7input.txt'

with open(filename) as fp:
    content = fp.readlines()


# for the ALL questions must be answered the same, we need the line breaks to determine different people in a group

bagsetall = []
bagindex = []
removechar = ['bags', 'bag', '.', ' ', '\n']
bagnum = []

for i in range(len(content)):
    bagline = content[i].split(' bags contain')
    a = re.split(r'\D+', bagline[1])
    b = []
    for k in range(len(a)):
        if a[k] != '':
            b.append(int(a[k]))            
    bagnum.append(b)
    for n in removechar: 
        bagline[0] = bagline[0].replace(n,'')
        bagline[1] = bagline[1].replace(n,'')
        bagline[0] = re.sub(r'\d+', '', bagline[0])
        bagline[1] = re.sub(r'\d+', '', bagline[1])
        bagnest = bagline[1].split(',')
    bagsetall.append(bagnest)
    bagindex.append(bagline[0])

# this recursively looks at each bag, and what bags can be in those bags, and what bags can be in those bags- it counts every time a new bag appears

factor = 1
counter = []    
def nestingdoll(baglist, goldcounter, bagindex, bagsetall, factor):
    if baglist != 'noother':
        baglistnew = bagsetall[bagindex.index(baglist)]
        counter.append(factor*sum(bagnum[bagindex.index(baglist)]))
        for m in range(len(baglistnew)):
            if baglistnew[m] != 'noother':
                nestingdoll(baglistnew[m], goldcounter, bagindex, bagsetall, factor*bagnum[bagindex.index(baglist)][m])

                

nestingdoll('shinygold', goldcounter, bagindex, bagsetall, factor)

print('the number of total bags is: '+ str(sum(counter)))
        
