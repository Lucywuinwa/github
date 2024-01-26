import sys
import pandas as pd

#start = int(sys.argv[1])
#stop = int(sys.argv[2])
df= pd.read_csv("president_heights.csv")

#df = df.iloc[start:stop, :]



def president_height(x,y):
    x = int(x)
    y = int(y)
    result = df.iloc[x:y,1].mean(axis=0) 
    return result
x = sys.argv[1]
y = sys.argv[2]
result = president_height(x,y)
print(f'The average height of presidents number {x} to {y} is {result:.2f}')