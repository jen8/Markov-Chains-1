from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()
    return text_string.rstrip()

open_and_read_file("green-eggs.txt")

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    #loop over the words in our string
    words = text_string.split()
    for index in range(len(words)-2): #-2 will stop after Sam I which is the last key we want 
        current_key = (words[index], words[index+1]) #would you
        chosen_word = words[index+2] #could or like
        if current_key not in chains:
            chains[current_key] = [chosen_word]
        else: #(we havent added this key to the chains yet)
            chains[current_key] = chains.get(current_key, None) + [chosen_word]
    return chains #not print because we cant use the value of chains in the following function

# input_path = open_and_read_file("green-eggs.txt")
# make_chains(input_path) #calling the function within the next function INCEPTION

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    current_key = choice(chains.keys())
    while True: 
        if current_key not in chains:
            text += " " + current_key[1]
            break
        else:
            print "Choosing a key from dict", current_key
            second_word_key = current_key[1]
            print "Printing the second word in the tuple", second_word_key
            text += " " + second_word_key

            new_second_word_value = choice(chains[current_key])
            print "Printing the random value from the first key chosen", new_second_word_value
            current_key = (second_word_key, new_second_word_value) #make a tuple
            print "This is the new key to go through our for loop", current_key
       
    return text


    #append that random word to second_word_key
    #assign second_word_key + random word into the new key for the program to look for for the next
    # #take the second word of current_key and append a random word 
    # text = str(random_word) + second_word_key 
    # print random_word
    # print second_word_key
    # print new_word_pair
    # #look for the key made of the tuple in the dictionary 


    #return random_word


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
