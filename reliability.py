import numpy as np
from itertools import combinations

def KrippendorffAlpha(data,datatype): 
    
    #determine min & max values
    Values = np.unique(data)
    missing = [99]
    Values = np.setdiff1d(Values, missing)

    minvalue = Values[0]
    maxvalue = Values[-1]

    #create a values-by-units matrix: 
    values_by_units = np.zeros(((maxvalue - minvalue + 1),len(data[0])))
    for row in data:
        for idx,i in enumerate(row):
            if i != missing: 
                values_by_units[i-minvalue,idx] += 1
    #reverse data diagonally: 
    data_reversed = np.swapaxes(data,0,1)
    #remove units with only 1 rating:
    values_by_units = np.swapaxes(values_by_units,0,1)
    for idx, i in enumerate(values_by_units):
        if np.sum(i) == 1: 
            values_by_units = np.delete(values_by_units, idx, 0)
    values_by_units = np.swapaxes(values_by_units,0,1)
    
    #list with sums for each value
    sumRow = np.sum(values_by_units, axis = 1)

    if Type == 'nominal':   
        
        diffExp = 0  
        for combination in list(combinations(sumRow,2)):
            diffExp += combination[0] * combination[1]
        
        diffObs = 0
        for unit in data_reversed: 
            for combination in list(combinations(unit,2)):
                if missing not in combination and combination[0] != combination[1]:
                    diffObs += 1 / (len(unit) - 1)
    
    elif Type == 'ordinal': 
        
        diffExp = 0  
        for idx, i in enumerate(sumRow):
            for j in range(idx+2,len(sumRow)+1): 
                combination = sumRow[idx:j]
                Metric = np.sum(combination) - ((combination[0] + combination[-1])/2) 
                diffExp += combination[0] * combination[-1] * Metric ** 2
        
        diffObs = 0
        for unit in data_reversed: 
            for idx, i in enumerate(unit):
                for j in range(idx, len(unit)):
                    combination = [i,unit[j]]
                    combination = sorted(combination)
                    if missing not in combination and combination[0] != combination[1]:
                        sumList = sumRow[combination[0]-minvalue:combination[1]-minvalue+1]
                        Metric = np.sum(sumList) - ((sumList[0] + sumList[-1])/2)
                        diffObs += (Metric ** 2) / (len(unit) - 1)

    elif Type == 'interval':   
       
        distances = []
        x = len(sumRow)
        while x > 0: #this while loop returns distances for each combination of sumRow numbers
            x = x-1
            for i in range(x):
                distances.append(i+1)
        
        diffExp = 0  
        for idx, combination in enumerate(list(combinations(sumRow,2))):
            diffExp += combination[0] * combination[1] * (distances[idx] ** 2)
        
        diffObs = 0
        for unit in data_reversed: 
            for combination in list(combinations(unit,2)):
                if missing not in combination:
                    diffObs += ((combination[0] - combination[1]) ** 2) / (len(unit) - 1)

    elif Type == 'ratio':   
     
        diffExp = 0  
        
        for idx, i in enumerate(sumRow):
            for j in range(idx, len(sumRow)):
                if idx != j: 
                    Eq = (Values[idx] - Values[j]) ** 2 / (Values[idx] + Values[j]) ** 2
                    diffExp += i * sumRow[j] * Eq
       
        diffObs = 0
        for unit in data_reversed: 
            for combination in list(combinations(unit,2)):
                if combination[0] != combination[1]: 
                    if missing not in combination: 
                        diffObs += (((combination[0] - combination[1]) ** 2/(combination[0] + combination[1]) ** 2)) / (len(unit) - 1)
 
    Alpha = 1 - (np.sum(sumRow)-1) * (diffObs / diffExp)
    return(Alpha)

a = [1,2,3,3,2,1,4,1,2,99,99,99]
b = [1,2,3,3,2,2,4,1,2,5,99,3]
c = [99,3,3,3,2,3,4,2,2,5,1,99]
d = [1,2,3,3,2,4,4,1,2,5,1,99]

data = np.vstack((a,b,c,d))
datatype = 'ratio'

print(KrippendorffAlpha(data,datatype))
    
    
