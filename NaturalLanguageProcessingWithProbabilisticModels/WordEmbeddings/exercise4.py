# UNIT TEST COMMENT: Candidate for Table Driven Tests
# UNQ_C4 GRADED FUNCTION: back_prop
def back_prop(x, yhat, y, h, W1, W2, b1, b2, batch_size):
    '''
    Inputs: 
        x:  average one hot vector for the context 
        yhat: prediction (estimate of y)
        y:  target vector
        h:  hidden vector (see eq. 1)
        W1, W2, b1, b2:  matrices and biases  
        batch_size: batch size 
     Outputs: 
        grad_W1, grad_W2, grad_b1, grad_b2:  gradients of matrices and biases   
    '''
    ### START CODE HERE (Replace instanes of 'None' with your code) ###
    # Compute l1 as W2^T (Yhat - Y)
    # and re-use it whenever you see W2^T (Yhat - Y) used to compute a gradient
    l1 = np.dot(W2.T,(yhat - y))
    
    relu = lambda x: x * (x > 0)

    # compute the gradient for W1
    grad_W1 = (1/batch_size)*np.dot(relu(np.dot(W2.T, yhat - y)), x.T)

    # Compute gradient of W2
    grad_W2 = (1/batch_size)*np.dot(yhat - y, h.T)
    
    # compute gradient for b1
    grad_b1 = np.sum((1/batch_size)*relu(np.dot(W2.T, yhat - y)),axis=1,keepdims=True)

    # compute gradient for b2
    grad_b2 = np.sum((1/batch_size)*(yhat - y),axis=1,keepdims=True)
    ### END CODE HERE ####
    
    return grad_W1, grad_W2, grad_b1, grad_b2