import numpy as np

#first, create dataset by merging lists with annotations by individual persons. Input data needs to be numerical for all data types. 
a = [1,2,3,3,2,1]
b = [1,4,3,5,5,4]
c = [1,2,3,3,2,1]


data = np.vstack((a,b,c))
Type = 'interval'
#insert def here

#create variables of data dimensions
nObserver = len(data)
nUnit = len(data[0])
nTotal = nObserver*nUnit
Min = np.amin(data)
Max = np.amax(data)
#create a total length for negative min values

#create a values-by-units matrix: 
data2 = np.zeros((Max,nUnit))
for row in data:
    for idx,i in enumerate(row):
        data2[i-1,idx] += 1

#aggregate to sum scores
sumColumn = np.sum(data2, axis = 0)
print(sumColumn)
sumRow = np.sum(data2, axis = 1)
print(sumRow)
Total = np.sum(sumRow)
print(Total)

nCombinations = np.sum(np.arange(len(sumRow)))

if Type == 'interval':
    diffExp = 0   
    for idx,s in enumerate(sumRow):
        for i in range(idx+1,len(sumRow)):
            diffExp += s*sumRow[i]*(i^2)
    
    diffObs = 0
    
    print(diffExp)

#KrippendorffAlpha = 1 - (Total-1) * (diffObs / diffExp)
