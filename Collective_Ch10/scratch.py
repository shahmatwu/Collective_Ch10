from numpy import *

def difcost(a, b):
    dif = 0
    # Loop over every row and col in matrix
    for i in range(shape(a)[0]): # loop over rows (1st dimension)
        for j in range(shape(a)[1]): # loop over cols (2nd dimension)
            # Square and sum the diffs
            dif += pow(a[i,j] - b[i,j], 2)
    return dif