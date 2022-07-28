# UNQ_C1 GRADED FUNCTION: process_data
def process_data(file_name):
    """
    Input: 
        A file_name which is found in your current directory. You just have to read it in. 
    Output: 
        words: a list containing all the words in the corpus (text file you read) in lower case. 
    """
    words = [] # return this variable correctly

    ### START CODE HERE ### 
    with open(file_name) as f:
        #Open the file, read its contents into a string variable
        file_name_data = f.read()
        
        # convert all letters to lower case
        file_name_data=file_name_data.lower()
        
        #Convert every word to lower case and return them in a list.
        words = re.findall('\w+',file_name_data)
    
    
    
    

    
    ### END CODE HERE ###
    
    return words