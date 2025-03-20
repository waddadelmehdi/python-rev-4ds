#%%
from math import log
lx1=list(range(2,1000,2))
lx2=[log(x) for x in lx1]
print(lx1)
print(lx2)

# %%

import random
max=1000
x=max*random.random()
print(x)

#%%
import random
import time

def getMatrice(size,maxVal):
    return [[maxVal*random.random() for _ in range(size)] for _ in range(size)]
def dotMatrices(mat1,mat2):
    size=len(mat1)
    res=[[0]*size]*size
    for i in range(size):
        for j in range(size):
            for k in range(size):
                res[i][j]+=mat1[i][k]*mat2[k][j]
    return res

def evalEfficency(algo,mat1,mat2):
    start=time.perf_counter_ns()
    res=algo(mat1,mat2)
    end=time.perf_counter_ns()
    ecart=(end-start)/(10**9)
    return res,ecart


n=500
maxVal=20
matA=getMatrice(n,maxVal)
matB=getMatrice(n,maxVal)
tempCalcul,matR=evalEfficency(dotMatrices,matA,matB)
print(matR)
print(f'time : {tempCalcul} sec')

#%%

l=[[0]*10]*10
print(l)

# %%
