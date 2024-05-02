# Function 
def word_replacement():
    string = 'We are going to replace one word of this sentence' # String we are gonna replace one word for
    
    word_to_replace = input('Choose the word from the sentece to replace: ') # Word we are going to replace from the sentece
    
    if word_to_replace in string: # Let's do an if statement to know there is a correct character/word to replace in the string
        
        new_word = input('Choose the new word: ') # Word we are going to use as replacement
        
        string = string.replace(word_to_replace, new_word) # Finally replace it if it exists
        
    else:
        print('Choose a valid word from the string') # In case the character/word doesn't exist we print this
    return string

print(word_replacement()) # We call the function to check if everything works correctly