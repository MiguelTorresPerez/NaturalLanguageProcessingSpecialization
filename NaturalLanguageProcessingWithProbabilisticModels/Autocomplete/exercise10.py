# UNQ_C10 GRADED FUNCTION: calculate_perplexity
def calculate_perplexity(sentence, n_gram_counts, n_plus1_gram_counts, vocabulary_size, start_token='<s>', end_token = '<e>', k=1.0):
    """
    Calculate perplexity for a list of sentences
    
    Args:
        sentence: List of strings
        n_gram_counts: Dictionary of counts of n-grams
        n_plus1_gram_counts: Dictionary of counts of (n+1)-grams
        vocabulary_size: number of unique words in the vocabulary
        k: Positive smoothing constant
    
    Returns:
        Perplexity score
    """
    # length of previous words
    n = len(list(n_gram_counts.keys())[0]) 
    
    # prepend <s> and append <e>
    sentence = [start_token] * n + sentence + [end_token]
    
    # Cast the sentence from a list to a tuple
    sentence = tuple(sentence)
    
    # length of sentence (after adding <s> and <e> tokens)
    N = len(sentence)
    
    # The variable p will hold the product
    # that is calculated inside the n-root
    # Update this in the code below
    product_pi = 1.0
    
    ### START CODE HERE ###
    
    # Index t ranges from n to N - 1, inclusive on both ends
    for t in range(N - n):

        # get the n-gram preceding the word at position t
        n_gram = sentence[t:t+n]
        
        # get the word at position t
        word = sentence[t+n]
        
        # Estimate the probability of the word given the n-gram
        # using the n-gram counts, n-plus1-gram counts,
        # vocabulary size, and smoothing constant
        probability = estimate_probability(word, n_gram, n_gram_counts, n_plus1_gram_counts,vocabulary_size, k=1)
        
        # Update the product of the probabilities
        # This 'product_pi' is a cumulative product 
        # of the (1/P) factors that are calculated in the loop
        product_pi *= 1 / probability
        ### END CODE HERE ###

    # Take the Nth root of the product
    perplexity = (product_pi)**(1/float(N))
    
    ### END CODE HERE ### 
    return perplexity