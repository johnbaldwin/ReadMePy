import numpy as np

def RemoveNonvariant(tab):
    '''

    This function assumes that tab is an array. Still need
    to convert int to double when x.astype(double) isn't
    working
    '''
    ncols = len(tab[0]) # Assumes tab is an array
    i = 3
    while(i < ncols):
        i += 1
        m = np.mean(tab[:,i]) # convert int to double here??
        if(m == 1 or m == 0):
            # missing a step here where column in array is 
            # removed
            tab = tab[:,-i]
            i -= 1
            ncols -= 1
    return tab


