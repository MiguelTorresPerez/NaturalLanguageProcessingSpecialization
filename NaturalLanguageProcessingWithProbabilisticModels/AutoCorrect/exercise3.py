# UNQ_C3 GRADED FUNCTION: get_probs
def get_probs(word_count_dict):
    '''
    Input:
        word_count_dict: The wordcount dictionary where key is the word and value is its frequency.
    Output:
        probs: A dictionary where keys are the words and the values are the probability that a word will occur. 
    '''
    probs = {}  # return this variable correctly
    
    ### START CODE HERE ###
    m = sum(word_count_dict.values())
    # get the total count of words for all words in the dictionary
    for key in word_count_dict.keys():
        probs[key] = word_count_dict[key] / m
    ### END CODE HERE ###
    return probs