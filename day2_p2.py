import pandas as pd
import numpy as np

filename = 'day2input.txt'

pwdata = pd.read_csv (filename, delimiter = ' ', header=None)

boolpw=[]
boolpw = [0 for n in range(len(pwdata))]
for i in range(len(pwdata)):
    col1=pwdata.iloc[i,0]
    col2=pwdata.iloc[i,1]
    col3=pwdata.iloc[i,2]
    stringloc=[int(b) for b in col1.split('-') if b.isdigit()]
    if col3[stringloc[0]-1] != col2[0] and col3[stringloc[1]-1] != col2[0]:
        boolpw[i]=0
    elif col3[stringloc[0]-1] == col2[0] and col3[stringloc[1]-1] == col2[0]:
        boolpw[i]=0
    else:
        boolpw[i]=1
            
    

print(sum(boolpw))