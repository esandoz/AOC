import re 
filename = 'day7input.txt'

with open(filename) as fp:
    content = fp.readlines()


# for the ALL questions must be answered the same, we need the line breaks to determine different people in a group

bagsetall = []
bagindex = []
removechar = ['bags', 'bag', '.', ' ', '\n']


for i in range(len(content)):
    bagline = content[i].split(' bags contain')
    for n in removechar:
        bagline[0] = bagline[0].replace(n,'')
        bagline[1] = bagline[1].replace(n,'')
        bagline[0] = re.sub(r'\d+', '', bagline[0])
        bagline[1] = re.sub(r'\d+', '', bagline[1])
        bagnest = bagline[1].split(',')
    bagsetall.append(bagnest)
    bagindex.append(bagline[0])

# this recursively looks at each bag, and what bags can be in those bags, and what bags can be in those bags- it counts every time 'shinygold' bags appear
goldcounter = 0    
def nestingdoll(baglist, goldcounter, bagindex, bagsetall):
    ender =['noother']*len(baglist)

    if baglist == ender:
        return goldcounter
    else:
        goldcounter = goldcounter + baglist.count('shinygold')
        outbaglist = []
        for m in range(len(baglist)):
            if baglist[m] != 'noother':
                outbaglist = outbaglist + bagsetall[bagindex.index(baglist[m])]
        return nestingdoll(outbaglist, goldcounter, bagindex, bagsetall)

        
goldspercolor = []       
for j in range(len(bagindex)):    
    goldspercolor.append(nestingdoll(bagsetall[j], goldcounter, bagindex, bagsetall))

counter = [0]*len(goldspercolor)
for j in range(len(goldspercolor)):
    if goldspercolor[j] > 0:
        counter[j] = 1
    else: 
        counter[j] = 0

print(sum(counter))
        
