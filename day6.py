
filename = 'day6input.txt'

declaredoc=[]
declareset = []
declaredocall = []
lineold = ''
with open(filename) as fp:
    content = fp.readlines()

# this combines multiple lines for documents into a single element with the blank line '\n' as the delimiter
# however, when it reaches the last line it needs to add the previous lines
for i in range(len(content)):
    if content[i] == '\n':
        declaredoc.append(lineold)
        declareset.append(len(set(lineold)))
        #set is a powerful tool that reports unique characters
        lineold = ''
    else: 
        lineold = lineold + content[i]
        lineold = lineold.strip('\n')
        
# the input script doesn't end on a line break, '\n' so the last row needs to be filled:  
declaredoc.append(lineold)
declareset.append(len(set(lineold)))

print(sum(declareset))

lineold = ''
# for the ALL questions must be answered the same, we need the line breaks to determine different people in a group
declaresetall =[]
for i in range(len(content)):
    if content[i] == '\n':
        declaredocall.append(lineold)
        groupdocs = lineold.splitlines() # this converts a string with linebreaks into a list
        for n in range(len(groupdocs)):
            if n == 0:
                groupset = set(groupdocs[n])
            else: groupset = groupset.intersection(set(groupdocs[n]))
        #set is a powerful tool that reports unique characters
        declaresetall.append(len(groupset))
        lineold = ''
    else: 
        lineold = lineold + content[i]
# the input script doesn't end on a line break, '\n' so the last row needs to be filled:  
groupdocs = lineold.splitlines()
for n in range(len(groupdocs)):
            if n == 0:
                groupset = set(groupdocs[n])
            else: groupset = groupset.intersection(set(groupdocs[n]))      
declaredocall.append(lineold)
declaresetall.append(len(groupset))

print(sum(declaresetall))



