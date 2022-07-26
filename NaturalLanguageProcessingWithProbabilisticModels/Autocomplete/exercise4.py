# UNIT TEST COMMENT: Candidate for Table Driven Tests 
### UNQ_C4 GRADED_FUNCTION: count_words ###
def count_words(tokenized_sentences):
    """
    Count the number of word appearence in the tokenized sentences
    
    Args:
        tokenized_sentences: List of lists of strings
    
    Returns:
        dict that maps word (str) to the frequency (int)
    """
            
    word_counts = {}
    ### START CODE HERE ###
    
    # Loop through each sentence
    for sentence in tokenized_sentences: # complete this line
        
        # Go through each token in the sentence
        for token in sentence: # complete this line

            # If the token is not in the dictionary yet, set the count to 1
            if token not in word_counts: # complete this line with the proper condition
                word_counts[token] = 1
            
            # If the token is already in the dictionary, increment the count by 1
            else:
                word_counts[token] += 1

    ### END CODE HERE ###
    
    return word_counts