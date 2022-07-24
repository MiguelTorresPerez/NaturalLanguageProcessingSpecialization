
# UNQ_C2 GRADED FUNCTION: gradientDescent

cc = lambda x, y, theta, m : (np.sum(np.square( ( np.dot(x,theta) - y ) ))) / (2 * m) 

def gradientDescent(x, y, theta, alpha, num_iters):
    '''
    Input:
        x: matrix of features which is (m,n+1)
        y: corresponding labels of the input matrix x, dimensions (m,1)
        theta: weight vector of dimension (n+1,1)
        alpha: learning rate
        num_iters: number of iterations you want to train your model for
    Output:
        J: the final cost
        theta: your final weight vector
    Hint: you might want to print the cost to make sure that it is going down.
    '''
    ### START CODE HERE ###
    # get 'm', the number of rows in matrix x
    m = x.shape[0]

    
    for i in range(0,num_iters):
        
        h = sigmoid(np.dot(x,theta))

        J = -1/m * (np.dot(y.T, np.log(h)) + np.dot((1-y).T,np.log(1-h)))  
        
        theta = theta - (alpha/m) * np.dot(x.T,(h-y))
        
    ### END CODE HERE ###
    J = float(J)
    return J, theta