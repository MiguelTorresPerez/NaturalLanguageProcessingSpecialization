# UNIT TEST COMMENT: Candidate for Table Driven Tests 
### UNQ_C5 GRADED_FUNCTION: get_words_with_nplus_frequency ###
def get_words_with_nplus_frequency(tokenized_sentences, count_threshold):
    """
    Find the words that appear N times or more
    
    Args:
        tokenized_sentences: List of lists of sentences
        count_threshold: minimum number of occurrences for a word to be in the closed vocabulary.
    
    Returns:
        List of words that appear N times or more
    """
    # Initialize an empty list to contain the words that
    # appear at least 'minimum_freq' times.
    closed_vocab = []
    
    # Get the word couts of the tokenized sentences
    # Use the function that you defined earlier to count the words
    word_counts = count_words(tokenized_sentences)
    
    ### START CODE HERE ###
#   UNIT TEST COMMENT: Whole thing can be one-lined with list comprehension
#   filtered_words = None

    # for each word and its count
    for word, cnt in word_counts.items(): # complete this line
        
        # check that the word's count
        # is at least as great as the minimum count
        if cnt >= count_threshold: # complete this line with the proper condition
            
            # append the word to the list
            closed_vocab.append(word)
    ### END CODE HERE ###
    
    return closed_vocab