import re
import numpy as np
filename = 'day14input.txt'

with open(filename) as fp:
    content = fp.readlines()
fp.close()


def masker(masknum, numbertoconvert):
    binarynum = '{0:036b}'.format(numbertoconvert)
    for i in range(len(masknum)):
        if masknum[i] != 'X':
            newstring = binarynum[:i] + masknum[i] + binarynum[i+1:]
            binarynum = newstring
    decimalnum = int('0b'+binarynum,2)
    return decimalnum

memlist = np.array([[0,0]])
for line in range(len(content)):
    if 'mask' in content[line]:
        masknum = content[line].split(" = ")[1].replace('\n','')
    else:
        memoryloc = int(re.sub("[^0-9]", "", content[line].split(" = ")[0]))
        decimalnum = int(content[line].split(" = ")[1])
        
        if memoryloc in memlist[:,0]:
            itemindex = np.where(memlist == memoryloc)
            memlist[itemindex[0],1] = masker(masknum, decimalnum)
        else:
            memlist=np.append(memlist,[[memoryloc, masker(masknum, decimalnum)]], axis=0)

print('the sum of the values is: ' + str(sum(memlist[:,1])))


def recursiveaddress(masknum, memorylocalbinary, digitstart, totaladdress):
    binarynum = memorylocalbinary
    if digitstart <= len(masknum):
        for i in range(digitstart, len(masknum)):
            if masknum[i] == '1':
                binarynum = binarynum[:i] + masknum[i] + binarynum[i+1:]
            elif masknum[i] == 'X':
                newstring1 = binarynum[:i] + '0' + binarynum[i+1:]
                newstring2 = binarynum[:i] + '1' + binarynum[i+1:]
                if i != len(masknum)-1:
                    recursiveaddress(masknum, newstring1, i+1, totaladdress)
                    recursiveaddress(masknum, newstring2, i+1, totaladdress)
                else:
                    totaladdress.append(newstring1)
                    totaladdress.append(newstring2)
                           
        totaladdress.append(binarynum)

                
    return(totaladdress)

adlist = np.array([['0',0]])
for line in range(len(content)):
    if 'mask' in content[line]:
        masknum = content[line].split(" = ")[1].replace('\n','')
    else:
        memoryloc = int(re.sub("[^0-9]", "", content[line].split(" = ")[0]))
        binad =  '{0:036b}'.format(memoryloc)
        final = recursiveaddress(masknum, binad, 0,[])
        # this is sloppy, my recursive algorithm redundantly produces some of the addresses, so I have to manually remove redundancies
        addresses = []
        for k in final:
            if k not in addresses:
                addresses.append(k)
        addressvalue = int(content[line].split(" = ")[1])
        for addressi in range(len(addresses)):
            if addresses[addressi] in adlist[:,0]:
                itemindex = np.where(adlist == addresses[addressi])
                for indexi in range(len(itemindex[0])):
                    adlist[itemindex[0][indexi],1] = addressvalue
            else:
#                adlist.append([addresses[addressi],addressvalue])
               adlist=np.append(adlist,[[addresses[addressi],int(addressvalue)]], axis=0)
summer = []
for i in range(len(adlist)):
    summer.append(int(adlist[i,1]))

print(' the sum of the new addresses is: ' + str(sum(summer)))

        