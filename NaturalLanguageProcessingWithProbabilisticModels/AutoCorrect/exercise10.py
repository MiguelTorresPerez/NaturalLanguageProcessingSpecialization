# UNIT TEST COMMENT: Candidate for Table Driven Tests
# UNQ_C10 GRADED FUNCTION: get_corrections
def get_corrections(word, probs, vocab, n=2, verbose = False):
    '''
    Input: 
        word: a user entered string to check for suggestions
        probs: a dictionary that maps each word to its probability in the corpus
        vocab: a set containing all the vocabulary
        n: number of possible word corrections you want returned in the dictionary
    Output: 
        n_best: a list of tuples with the most probable n corrected words and their probabilities.
    '''
    
    suggestions = []
    n_best = []
    
    ### START CODE HERE ###
    
    #Step 1, 2: create suggestions as described above and determine probability of suggestions
    
    #
    suggestions = [(word, probs[word])] if word in vocab else [(m, probs[m]) for m in edit_one_letter(word) & vocab] or [(m, probs[m]) for m in edit_two_letter(word) & vocab]
    
    #Step 3: Get all your best words and return the most probable top n_suggested words as n_best
    
    #key used to sort following probability criteria, and reverse transform it to descending
    # [:n] finally splits the list and returns the most n probable words
    
    # ?? could we use instead word proability inferred from zipf's law frecuency of words on corpus ??
    n_best = sorted(suggestions, key = lambda x : x[1], reverse = True)[:n]

    ### END CODE HERE ###
    
    if verbose: print("entered word = ", word, "\nsuggestions = ", suggestions)

    return n_best