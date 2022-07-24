# UNQ_C3 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
def compute_loss(X, Y, R):
    '''
    Inputs: 
        X: a matrix of dimension (m,n) where the columns are the English embeddings.
        Y: a matrix of dimension (m,n) where the columns correspong to the French embeddings.
        R: a matrix of dimension (n,n) - transformation matrix from English to French vector space embeddings.
    Outputs:
        L: a matrix of dimension (m,n) - the value of the loss function for given X, Y and R.
    '''
    ### START CODE HERE ###
    # m is the number of rows in X
    m = X.shape[0]
        
    # diff is XR - Y    
    diff = np.dot(X,R)-Y

    # diff_squared is the element-wise square of the difference    
    diff_squared = diff**2

    # sum_diff_squared is the sum of the squared elements
    sum_diff_squared = np.sum(diff_squared)

    # loss i is the sum_diff_squard divided by the number of examples (m)
    loss = sum_diff_squared/m
    ### END CODE HERE ###
    return loss