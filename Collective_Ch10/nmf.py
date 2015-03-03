from numpy import *

def difcost(a, b):
    """ Return Euclidean distance between matrices, a and b
        which is sum of square of differences """

    # I'm substituting the book's loops with my own version using numpy functions
    #dif = 0
    ## Loop over every row and col in matrix
    #for i in range(shape(a)[0]): # loop over rows (1st dimension)
    #    for j in range(shape(a)[1]): # loop over cols (2nd dimension)
    #        # Square and sum the diffs
    #        dif += pow(a[i,j] - b[i,j], 2)

    return sum(power(a - b, 2))

def factorize(v, pc = 10, iter = 50):
    """ v is matrix to be factorized
        pc is number of features to find - needs experimentation/tuning
        iter is number of iterations """
    ic = shape(v)[0] # no of rows
    fc = shape(v)[1] # no of cols
    epsilon = 0.000000001

    # Initialize the weight and feature matrices w random vals
    w = matrix([[random.random() for j in range(pc)] for i in range(ic)])
    h = matrix([[random.random() for j in range(fc)] for i in range(pc)])

    # Perform operation a max of iter times
    for i in range(iter):
        wh = w * h

        # Get current cost
        cost = difcost(v, wh)

        if i % 10 == 0: print(cost)

        # Terminate if the matrix has been fully factorized
        if cost==0: break

        """ As of D. Shrestha, "Document Clustering Through Non-Negative Matrix Factorization: A Case Study
        of Hadoop for Computational Time Reduction of Large Scale Documents.," pp. 1-10. The parameter epsilon << 1
        is added to the multiplicative update rule to avoid division by zero, thus avoiding a NaN in the algorithm.
        This is added to: wd=(w*h*transpose(h))+0.000000001 and hd=(transpose(w)*w*h)+0.000000001
        http://www.oreilly.com/catalog/errataunconfirmed.csp?isbn=9780596529321 """ 

        # Update feature matrix
        hn = (transpose(w) * v)
        hd = (transpose(w) * w * h) + epsilon

        h = matrix(array(h) * array(hn) / array(hd))

        # Update weights matrix
        wn = (v * transpose(h))
        wd = (w * h * transpose(h)) + epsilon

        w = matrix(array(w) * array(wn) / array(wd))

    return w, h