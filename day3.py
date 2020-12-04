import pandas as pd

filename = 'day3input.txt'

ff=[1 for i in range(31)]
single_data = pd.read_fwf(filename, widths=ff, header=None)
num_tree_iterations = int(len(single_data)/31*7+1)

appended_tree_data = [single_data for b in range(num_tree_iterations)]
tree_data = pd.concat(appended_tree_data,axis=1)

treevar='#'

def treecounter(tree_data,numright,numdown):
    count_trees = [0 for n in range(len(tree_data))]
    j=0
    for i in range(0, len(tree_data),numdown):
        if tree_data.iloc[i,j] == treevar:
            count_trees[i]=1
        j=j+numright
    totcount = sum(count_trees)
    return totcount

slopes = [[1, 1],[1,3],[1,5],[1,7],[2,1]]
countiter = [0 for n in range(len(slopes))]

for l in range(len(slopes)):
    numdown=slopes[l][0]
    numright=slopes[l][1]
    countiter[l]=treecounter(tree_data,numright,numdown)

multiply=1
for n in range(len(countiter)):
    multiply = multiply*countiter[n]

print(countiter[1])
print(multiply)