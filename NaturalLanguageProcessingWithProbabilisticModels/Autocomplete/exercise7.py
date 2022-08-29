# UNIT TEST COMMENT: Candidate for Table Driven Tests 
### UNQ_C7 GRADED_FUNCTION: preprocess_data ###
def preprocess_data(train_data, test_data, count_threshold, unknown_token="<unk>", get_words_with_nplus_frequency=get_words_with_nplus_frequency, replace_oov_words_by_unk=replace_oov_words_by_unk):
    """
    Preprocess data, i.e.,
        - Find tokens that appear at least N times in the training data.
        - Replace tokens that appear less than N times by "<unk>" both for training and test data.        
    Args:
        train_data, test_data: List of lists of strings.
        count_threshold: Words whose count is less than this are 
                      treated as unknown.
    
    Returns:
        Tuple of
        - training data with low frequent words replaced by "<unk>"
        - test data with low frequent words replaced by "<unk>"
        - vocabulary of words that appear n times or more in the training data
    """
    ### START CODE HERE ###

    # Get the closed vocabulary using the train data
    vocabulary = get_words_with_nplus_frequency(train_data,count_threshold)
    
    # For the train data, replace less common words with "<unk>"
    train_data_replaced = replace_oov_words_by_unk(train_data,vocabulary,unknown_token)
    
    # For the test data, replace less common words with "<unk>"
    test_data_replaced = replace_oov_words_by_unk(test_data,vocabulary,unknown_token)
    
    ### END CODE HERE ###
    return train_data_replaced, test_data_replaced, vocabulary