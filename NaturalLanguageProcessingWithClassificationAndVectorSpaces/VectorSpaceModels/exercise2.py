# UNQ_C2 GRADED FUNCTION: euclidean

def euclidean(A, B):
    """
    Input:
        A: a numpy array which corresponds to a word vector
        B: A numpy array which corresponds to a word vector
    Output:
        d: numerical number representing the Euclidean distance between A and B.
    """

    ### START CODE HERE ###

    # euclidean distance 
    
    #we apply the l2 norm that is the distance of the vector coordinate from the origin of the vector space
    d = np.linalg.norm(A-B)

    ### END CODE HERE ###

    return d