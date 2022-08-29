# UNIT TEST COMMENT: Candidate for Table Driven Tests
# UNQ_C1 GRADED FUNCTION: initialize_model
def initialize_model(N,V, random_seed=1):
    '''
    Inputs: 
        N:  dimension of hidden vector 
        V:  dimension of vocabulary
        random_seed: random seed for consistent results in the unit tests
     Outputs: 
        W1, W2, b1, b2: initialized weights and biases
    '''
    
    ### START CODE HERE (Replace instances of 'None' with your code) ###
    np.random.seed(random_seed)
    # W1 has shape (N,V)
    W1 = np.random.random((N, V))
    
    # W2 has shape (V,N)
    W2 = np.random.random((V, N))
    
    # b1 has shape (N,1)
    b1 = np.random.random((N, 1))
    
    # b2 has shape (V,1)
    b2 = np.random.random((V, 1))
    
    ### END CODE HERE ###
    return W1, W2, b1, b2